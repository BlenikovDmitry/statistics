import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

df = pd.read_csv('bonds.csv', encoding = 'windows-1251')

df['Сумма купона'] = df['Сумма купона'].str.replace('-','0')
df['Сумма купона'] = df['Сумма купона'].str.replace(',','.')
df['Сумма купона'] = df['Сумма купона'].astype(np.float32)

#print(df['Сумма купона'])

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
    return (z_np2 / df[field].count()) * 100

#функция считает по сигмам
#если в сумме не 100%, значит есть пропуски в столбце
def count_sigmas(df,field):
    std1 = df[field].std()
    df['sigma'] = abs(df[field] - std1)
    sigma1 = df[(df['sigma'] < std1)]
    sigma2 = df[(df['sigma'] > std1) & (df['sigma'] < std1 * 2)]
    sigma3 = df[(df['sigma'] > std1 * 2) & (df['sigma'] < std1 * 3)]
    sigma4 = df[(df['sigma'] > std1 * 3) & (df['sigma'] < std1 * 4)]
    sigma5 = df[(df['sigma'] > std1 * 4) & (df['sigma'] < std1 * 5)]
    sigma5_1 = df[(df['sigma'] > std1 * 5)]
    print(f' В пределах 1 сигмы {sigma1.shape[0] / df.shape[0] * 100} %')
    print(f' В пределах 2 сигм {sigma2.shape[0] / df.shape[0] * 100} %')
    print(f' В пределах 3 сигм {sigma3.shape[0] / df.shape[0] * 100} %')
    print(f' В пределах 4 сигм {sigma4.shape[0] / df.shape[0] * 100} %')
    print(f' В пределах 5 сигм {sigma5.shape[0] / df.shape[0] * 100} %')
    print(f' Более 5 сигм: {sigma5_1.shape[0] / df.shape[0] * 100} %')

#диаграмма рассеивания - нужно протестить
#если x = y - можно понять, есть ли разрывы в данных и сходу сгруппировать визуально
def scatter(df, field, df1, field1):
    plt.figure(figsize = (6,4))
    plt.scatter(df[field], df1[field1], c = 'red', edgecolors = 'black')
    plt.title('Зависимость')
    plt.show()


#оценка хвостов - метод хилла
#отдельно нарисовать график qqplot для хвоста - чтобы понять,  можем ли использовать метод хилла
#берем натуральный логарифм от точки и сравниваем с экпоненциальным 
#распределением 

#можно потом обернуть в интерфейс streamlit и/или 
#ендпоинты fast api
