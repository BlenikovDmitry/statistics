import pandas as pd
import gc
import matplotlib.pyplot as plt
from bootstraping import bootstrap
import streamlit as st
import sys
#загрузчик файла сырых данных
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is None:
    sys.exit("Программа завершена")

#считывание сырых данных для обработки    
raw_set = pd.read_csv(uploaded_file, encoding = 'Windows-1251', sep=';')


#очистка и преобразование типов данных
raw_set['Дата'] = raw_set['Дата'].astype('string')
raw_set['Ключевая ставка, % годовых'] = raw_set['Ключевая ставка, % годовых'].str.replace(',', '.')
raw_set['Инфляция, % г/г'] = raw_set['Инфляция, % г/г'].str.replace(',', '.')
raw_set['Ключевая ставка, % годовых'] = raw_set['Ключевая ставка, % годовых'].astype('float32')
raw_set['Инфляция, % г/г'] = raw_set['Инфляция, % г/г'].astype('float32')
raw_set['Ключевая ставка, % годовых'] = raw_set['Ключевая ставка, % годовых'].round(2)
raw_set['Инфляция, % г/г'] = raw_set['Инфляция, % г/г'].round(2)
final_set = raw_set.loc[:, ['Дата', 'Ключевая ставка, % годовых', 'Инфляция, % г/г']]

del raw_set
gc.collect()
#интерфейс заголовка и подсчет корреляции по Пирсону и описательный анализ
st.header("Анализ ключевой ставки ЦБ и инфляции")
st.subheader("Описательный анализ")

correliation = final_set[['Ключевая ставка, % годовых', 'Инфляция, % г/г']].corr(method='pearson')
st.write(correliation)
desc = final_set.describe(include = ['float32']).astype('float32').round(2)
st.write(desc)
del desc
del correliation
gc.collect()

#график наложенных друг на друга инфляции и ключевой ставки
st.header("Графики")
fig, ax = plt.subplots(figsize=(25,10))
plt.title('Ключевая ставка / Инфляция')
plt.xlabel("месяц.год")
plt.ylabel("Ставка")

plt.xticks(rotation="vertical")
ax.plot(final_set['Дата'], final_set['Ключевая ставка, % годовых'], '-bo', linewidth=2, markersize=6, markerfacecolor='black')
ax.plot(final_set['Дата'], final_set['Инфляция, % г/г'], '-ro', linewidth=2, markersize=6, markerfacecolor='black')
plt.legend(['Ключевая ставка, % годовых', 'Инфляция, % г/г'])
ax.grid()
st.pyplot(fig)
plt.close()

#график бутстрапа ключевой ставки и стандартного отклонения чтобы понять распределение
st.subheader("Ключевая ставка: ")
count_iterations = 10000
distribution_average, distribution_stde, average, stde = bootstrap(final_set['Ключевая ставка, % годовых'], count_iterations)
fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot(2,1,1)
ax.set_title("Распределение среднего ключевой ставки")
ax.hist(distribution_average, 50, color = "red", ec="lightblue", edgecolor="black", rwidth = 5)
plt.axvline(average,linewidth=4, color='g', label = "Среднее изначальное")
plt.legend()
ax.grid()
ax = fig.add_subplot(2,1,2)
ax.set_title("Распределение стандартного отклонения ключевой ставки")
ax.hist(distribution_stde, 50, color = "lightblue", ec="red", edgecolor="black", rwidth = 5)
plt.axvline(stde,linewidth=4, color='g', label = "Среднее изначальное")

plt.legend()
ax.grid()
st.pyplot(fig)
plt.close()
#график бутстрапа инфляции и стандартного отклонения чтобы понять распределение
st.subheader("Инфляция: ")
distribution_average, distribution_stde, average, stde = bootstrap(final_set['Инфляция, % г/г'], count_iterations)
fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot(2,1,1)
ax.set_title("Распределение среднего инфляции")
ax.hist(distribution_average, 50, color = "green", ec="lightblue", edgecolor="black", rwidth = 5)
plt.axvline(average,linewidth=4, color='r', label = "Среднее изначальное")
plt.legend()
ax.grid()
ax = fig.add_subplot(2,1,2)
ax.set_title("Распределение стандартного отклонения инфляции")
ax.hist(distribution_stde, 50, color = "gray", ec="red", edgecolor="black", rwidth = 5)
plt.axvline(stde,linewidth=4, color='r', label = "Среднее изначальное")

plt.legend()
ax.grid()
st.pyplot(fig)
plt.close()
