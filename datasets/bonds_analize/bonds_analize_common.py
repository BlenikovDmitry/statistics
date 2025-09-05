import streamlit as st
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


st.header("Анализ облигаций общий")

#загрузчик файла сырых данных
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is None:
    sys.exit("Программа завершена")

#Читаем сырые файлы
raw_data = pd.read_csv(uploaded_file, encoding='windows-1251')
#выводим весь список
st.subheader("Весь список")
st.write(raw_data)
#отрисовываем доли валют в общей корзине
vals = []
labels = ["USD", "RUB", "EUR", "CNF", "CNY"]
vals.append((raw_data['Валюта номинала'] == 'USD').sum())
vals.append((raw_data['Валюта номинала'] == 'RUB').sum())
vals.append((raw_data['Валюта номинала'] == 'EUR').sum())
vals.append((raw_data['Валюта номинала'] == 'CNF').sum())
vals.append((raw_data['Валюта номинала'] == 'CNY').sum())

fig, ax = plt.subplots(figsize=(10,8))
ax.set_title("Доля валют в общей корзине")
plt.pie(vals, labels=labels, wedgeprops={'lw':1, 'ls':'--','edgecolor':"k"}, autopct='%1.1f%%')
st.pyplot(fig)
plt.close()


#формируем новый датафрейм для описательного анализа
#для этого очищаем данные и приводим к нужному типу
#иначе метод describe не сработает
desc_subset = raw_data[['Дох посл сделки', 'Цена закрытия']]

desc_subset['Дох посл сделки'] = desc_subset['Дох посл сделки'].str.replace(',', '.')
desc_subset['Цена закрытия'] = desc_subset['Цена закрытия'].str.replace(',', '.')

desc_subset['Дох посл сделки'] = desc_subset['Дох посл сделки'].str.replace('-', '0').astype('float32')
desc_subset['Цена закрытия'] = desc_subset['Цена закрытия'].str.replace('-', '0').astype('float32')


desc_subset['Дох посл сделки'] = desc_subset['Дох посл сделки'].replace(0, np.nan)
desc_subset['Цена закрытия'] = desc_subset['Цена закрытия'].replace(0, np.nan)
#выводим описательный анализ
st.subheader("Описательный анализ")
st.write(desc_subset.describe(include = ('float32')))    

#делаем еще датафрейм для подсчета топовых бумаг
top_papers_subset = pd.merge(raw_data[['Наименование', 'Сделок шт.']],desc_subset, left_index=True, right_index=True)
#top_papers_subset['Сделок шт.'] = top_papers_subset['Сделок шт.'].str.replace('-', '0').astype('float32')
top_papers_subset['Сделок шт.'] = top_papers_subset['Сделок шт.'].replace(0, np.nan)


#удаляем пустоту чтобы не набрать некорректных данных
top_papers_subset = top_papers_subset.dropna(subset=['Сделок шт.'])
top_papers_subset = top_papers_subset.dropna(subset=['Дох посл сделки'])
top_papers_subset = top_papers_subset.dropna(subset=['Цена закрытия'])
#выводим топ ликвидных(наибольшее число сделок)
likv_visual = st.checkbox("Топ 10 ликвидных")
if likv_visual:
    top_papers_subset = top_papers_subset.sort_values('Сделок шт.', ascending=False)
    st.subheader("Топ 10 ликвидных")
    top_papers_tmp = top_papers_subset.head(10)
    st.write(top_papers_tmp)
    #выводим столбцовый график ликвидных бумаг
    fig, ax = plt.subplots(figsize=(13,10))
    plt.xticks(rotation="vertical")
    ax.set_title("Распределение число сделок по выпускам")
    bars = ax.bar(top_papers_tmp['Наименование'], top_papers_tmp['Сделок шт.'], linewidth = 3.0, color = 'blue', ec='red')
    ax.bar_label(bars)
    ax.grid()
    st.pyplot(fig)
    plt.close()
#выводим топ доходных(самая высокая доха последней сделки)
top_doh_visual = st.checkbox("Топ 10 доходных")
if top_doh_visual:
    top_papers_subset = top_papers_subset.sort_values('Дох посл сделки', ascending=False)
    st.subheader("Топ 10 доходных")
    top_papers_tmp = top_papers_subset.head(10)
    st.write(top_papers_tmp)
    #выводим столбцовый график топовых доходностей
    fig, ax = plt.subplots(figsize=(13,10))
    plt.xticks(rotation="vertical")
    ax.set_title("Распределение дохода последней сделки по выпускам")
    bars = ax.bar(top_papers_tmp['Наименование'], top_papers_tmp['Дох посл сделки'], linewidth = 3.0, color = 'blue', ec='red')
    ax.bar_label(bars)
    ax.grid()
    st.pyplot(fig)
    plt.close()
#выводим самые дешевые (самая низкая цена)
low_price_visual = st.checkbox("Топ 10 дешевок")
if low_price_visual:
    top_papers_subset = top_papers_subset.sort_values('Цена закрытия')
    st.subheader("Топ 10 дешевых")
    top_papers_tmp = top_papers_subset.head(10)
    st.write(top_papers_tmp)
    #выводим столбцовый график топовых доходностей
    fig, ax = plt.subplots(figsize=(13,10))
    plt.xticks(rotation="vertical")
    ax.set_title("Распределение дохода последней сделки по выпускам")
    bars = ax.bar(top_papers_tmp['Наименование'], top_papers_tmp['Цена закрытия'], linewidth = 3.0, color = 'blue', ec='red')
    ax.bar_label(bars)
    ax.grid()
    st.pyplot(fig)
    plt.close()
