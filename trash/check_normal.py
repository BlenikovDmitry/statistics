import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

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

#функция построения квантиль - квантильного графика
#сравниваем с нормальным распределением
def qqplot(df, field):
    plt.figure(figsize = (6,4))
    stats.probplot(df[field], dist="norm", plot=plt)

    plt.title("Q-Q график (Проверка на нормальность)")
    plt.xlabel("Теоретические квантили")
    plt.ylabel("Выборочные квантили")
    plt.grid(True)
    plt.show()
    
#подсчет z оценок каждого из элементов
def z_scores(df, field):
    return stats.zscore(df[field])

#проверяем. сколько точек лежит вне 95% нормальности
def check_outliers(df, field):
    z_scores1 = z_scores(df, field)
    z_np2 = np.sum((z_scores1 > 1.96) | (z_scores1 < -1.96))
    return (z_np2 / df[field].sum()) * 100

print(str(check_outliers(df, 'Сумма купона')) + "%")

    
df = df[df['Сумма купона'] < 100]

qqplot(df,'Сумма купона')
#подсчет сигм и количества точек, которые туда попадают(до 5 сигм)
#диаграмма рассеяния

#оценка хвостов - метод хилла
#отдельно нарисовать график qqplot для хвоста - чтобы понять,  можем ли использовать метод хилла

#можно потом обернуть в интерфейс streamlit и/или 
#ендпоинты fast api

#другие показатели нормальности распределения
