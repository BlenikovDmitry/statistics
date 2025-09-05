import streamlit as st
import sys
import pandas as pd
import numpy as np


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
top_papers_subset['Сделок шт.'] = top_papers_subset['Сделок шт.'].str.replace('-', '0').astype('float32')
top_papers_subset['Сделок шт.'] = top_papers_subset['Сделок шт.'].replace(0, np.nan)


#удаляем пустоту чтобы не набрать некорректных данных
top_papers_subset = top_papers_subset.dropna(subset=['Сделок шт.'])
top_papers_subset = top_papers_subset.dropna(subset=['Дох посл сделки'])
top_papers_subset = top_papers_subset.dropna(subset=['Цена закрытия'])
#выводим топ ликвидных(наибольшее число сделок)
top_papers_subset = top_papers_subset.sort_values('Сделок шт.', ascending=False)
st.subheader("Топ 10 ликвидных")
st.write(top_papers_subset.head(10))
#выводим топ доходных(самая высокая доха последней сделки)
top_papers_subset = top_papers_subset.sort_values('Дох посл сделки', ascending=False)
st.subheader("Топ 10 доходных")
st.write(top_papers_subset.head(10))
#выводим самые дешевые (самая низкая цена)
top_papers_subset = top_papers_subset.sort_values('Цена закрытия')
st.subheader("Топ 10 дешевых")
st.write(top_papers_subset.head(10))
