import pandas as pd
import numpy as np

df = pd.read_csv('bonds.csv', encoding = 'windows-1251')

df['Сумма купона'] = df['Сумма купона'].str.replace('-','0')
df['Сумма купона'] = df['Сумма купона'].str.replace(',','.')
df['Сумма купона'] = df['Сумма купона'].astype(np.float32)

print(df['Сумма купона'])

#функция подсчета среднего, медианы, моды
#и разведочного анализа
def statistic(df, field):
    mean = df[field].mean()
    median = df[field].median()
    mode = df[field].mode()
    desc = df[field].describe()

    return (mean, median, mode, desc)


#отрисовка графика распределения(гистограмма)
#подсчет сигм и количества точек, которые туда попадают(до 20 сигм)
#квантиль - квантильный график
#оценка хвостов - метод хилла

#другие показатели нормальности распределения
