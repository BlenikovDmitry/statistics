import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import math

df = pd.read_csv('bonds.csv', encoding = 'windows-1251')

'''df['Сумма купона'] = df['Сумма купона'].str.replace('-','0')
df['Сумма купона'] = df['Сумма купона'].str.replace(',','.')
df['Сумма купона'] = df['Сумма купона'].astype(np.float32)'''

df['Значение'] = df['Значение'].str.replace(',','.')
df['Значение'] = df['Значение'].astype(np.float32)

#print(df['Сумма купона'])


#функция подсчета среднего, медианы
#и разведочного анализа
def statistic(df, field):
    mean = df[field].mean()
    median = df[field].median()
    desc = df[field].describe()

    return (mean, median, desc)

'''mean, median, desc = statistic(df, 'Значение')
print(mean)
print(median)
print(desc)'''

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
    print(f' В пределах 1 сигмы {sigma1.shape[0] / df.shape[0] * 100} %')
    print(f' От 1 до 2 сигм {sigma2.shape[0] / df.shape[0] * 100} %')
    print(f' От 2 до 3 сигм {sigma3.shape[0] / df.shape[0] * 100} %')
    print(f' От 3 до 4 сигм {sigma4.shape[0] / df.shape[0] * 100} %')
    print(f' От 4 до 5 сигм {sigma5.shape[0] / df.shape[0] * 100} %')
    print(f' Более 5 сигм: {sigma5_1.shape[0] / df.shape[0] * 100} %')
    
#пишем столбец с изменениями чтобы оценить риски
df['returns'] = df['Значение'].pct_change()
#count_sigmas(df, 'returns')
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
    plt.show()
#hill_graphic_check(df, 'returns')
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
#Пытаемся подобрать k, чтобы оценить распределение
for i in range(1,df['returns'].shape[0] - 5):
    print(hill_method(df, 'returns', i))
    
#можно потом обернуть в интерфейс streamlit и/или 
#ендпоинты fast api
