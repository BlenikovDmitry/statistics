import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import math
import streamlit as st

#подготовка данных и дополнили столбцом изменения в %
def prepare_data_field(df, field):
    df[field] = df[field].str.replace(',','.')
    df[field] = df[field].astype(np.float64).round(2)
    df['Изменение(%)'] = (df[field].pct_change() * 100).round(2)
    df.iloc[0,2] = 0.0



#функция подсчета среднего, медианы
#и разведочного анализа
def statistic(df, field):
    mean = df[field].mean()
    median = df[field].median()
    desc = df[field].describe().rename({
    'count': 'Количество',
    'mean': 'Среднее',
    'std': 'Станд. отклон.',
    'min': 'Минимум',
    '25%': '25-й перцентиль',
    '50%': 'Медиана',
    '75%': '75-й перцентиль',
    'max': 'Максимум'
    })
    desc = desc.round(2)

    return (mean, median, desc)


#функция построения квантиль - квантильного графика
#сравниваем с нормальным распределением
def qqplot(df, field):
    plt.figure(figsize = (6,4))
    stats.probplot(df[field], dist="norm", plot=plt)

    plt.title("Q-Q график (Проверка на нормальность)")
    plt.xlabel("Теоретические квантили")
    plt.ylabel("Выборочные квантили")
    plt.grid(True)
    return plt

#qqplot(df, 'Значение')
#подсчет z оценок каждого из элементов
def z_scores(df, field):
    return stats.zscore(df[field])

#проверяем. сколько точек лежит вне 95% нормальности
def check_outliers(df, field):
    z_scores1 = z_scores(df, field)
    z_np2 = np.sum((z_scores1 > 1.96) | (z_scores1 < -1.96))
    return (z_np2 / df[field].count()) * 100

#print(check_outliers(df, 'Значение'))
#функция считает по сигмам
#если в сумме не 100%, значит есть пропуски в столбце
def count_sigmas(df,field):
    std1 = df[field].std()
    mean_v = df[field].mean()
    df['sigma'] = abs(df[field] - mean_v) / std1
    sigma1 = df[(df['sigma'] < 1)]
    sigma2 = df[(df['sigma'] > 1) & (df['sigma'] < 2)]
    sigma3 = df[(df['sigma'] > 2) & (df['sigma'] < 3)]
    sigma4 = df[(df['sigma'] > 3) & (df['sigma'] < 4)]
    sigma5 = df[(df['sigma'] > 4) & (df['sigma'] < 5)]
    sigma5_1 = df[(df['sigma'] > 5)]
    st.write(f' В пределах 1 сигмы: {round(sigma1.shape[0] / df.shape[0] * 100,2)} %')
    st.write(f' От 1 до 2 сигм: {round(sigma2.shape[0] / df.shape[0] * 100,2)} %')
    st.write(f' От 2 до 3 сигм: {round(sigma3.shape[0] / df.shape[0] * 100,2)} %')
    st.write(f' От 3 до 4 сигм: {round(sigma4.shape[0] / df.shape[0] * 100,2)} %')
    st.write(f' От 4 до 5 сигм: {round(sigma5.shape[0] / df.shape[0] * 100,2)} %')
    st.write(f' Более 5 сигм: {round(sigma5_1.shape[0] / df.shape[0] * 100,2)} %')
    
#диаграмма рассеивания - нужно протестить
#если x = y - можно понять, есть ли разрывы в данных и сходу сгруппировать визуально
def scatter(df, field, df1, field1):
    plt.figure(figsize = (6,4))
    plt.scatter(df[field], df1[field1], c = 'red', edgecolors = 'black')
    plt.title('Зависимость')
    plt.show()
#оценка целесообразонсти применения метода хилла
#передаем то что кажется хвостом
#если хвост ложится около линии экспоненциального распределения
#значит можно
def hill_graphic_check(df, field):
    df['ln'] = np.log(df[field])
    plt.figure(figsize=(6,4))
    stats.probplot(df['ln'], dist=stats.expon, plot=plt)
    plt.title("Q-Q график (Проверка на нормальность)")
    plt.xlabel("Теоретические квантили")
    plt.ylabel("Выборочные квантили")
    plt.grid(True)
    return plt
'''
Если \(\gamma < 0.5\) (ваш случай): У вашего процесса существует конечная дисперсия (и конечное среднее). 
Это значит, что несмотря на наличие крупных выбросов, процесс всё ещё поддается классическому долгосрочному прогнозированию
Если бы \(\gamma \ge 0.5\): Дисперсия стала бы бесконечной. Стандартные методы (вроде метода наименьших квадратов, среднеквадратичного отклонения) перестали бы работать.
Если бы \(\gamma \ge 1\): У процесса не было бы даже математического ожидания (среднего значения). Каждое новое экстремальное значение полностью меняло бы среднее по всей истории.
Подходит для оценки изменений цены актива
'''
def hill_method(df, field, k):
    #убираем все значения nan и берем по модулю
    sorted_data = df[field].dropna()
    sorted_data = np.abs(sorted_data)
    #сортируем по убыванию
    sorted_data = np.sort(sorted_data)[::-1]
    #берем первые к элементов 
    top_k = sorted_data[:k]
    #берем k-й элемент
    k_1 = sorted_data[k]
    #применяем формулу метода Хилла
    result = np.mean(np.log(top_k / k_1))

    return result
#можно потом обернуть в ендпоинты fast api
