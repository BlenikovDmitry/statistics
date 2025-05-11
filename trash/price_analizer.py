import math
import statistics
import matplotlib.pyplot as plt
import csv
import random

"""
Анализ исторических значений
Рассчитываем среднее, медиану, стандартное отклонение

Бутстрапируем полученную выборку, отрисовываем распределение среднего и
стандартного отклонения(10.000 итераций)

!!!ВАЖНО
Хорошо работает на выборках, которые имеют ограниченный диапазон значений
Если диапазон широк, то может только показать общий тренд


"""


data = []
markers = []
average = 0
median = 0
stde = 0
count_iterations = 10000

def read(data, markers):
    with open("in.csv", 'r') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            markers.append(str(row[0]))
            data.append(float(row[1]))
        
        

def bootstrap():
    counter_iteration = 0
    counter = 0
    distribution_average = []
    distribution_median = []
    distribution_stde = []
    while counter_iteration < count_iterations:
        counter = 0
        markers_var = []
        data_var = []
        while counter < len(data):
            data_var.append(data[int(random.random() * len(data))])
            counter = counter + 1
       
        distribution_average.append(statistics.mean(data_var))
        distribution_stde.append(statistics.stdev(data_var))
    
        
        counter_iteration += 1
     
    fig = plt.figure(figsize=(6,6))
    ax = fig.add_subplot(2,2,1)
    ax.set_title("Распределение среднего")
    ax.hist(distribution_average, 50, color = "red", ec="lightblue", edgecolor="black", rwidth = 5)
    plt.axvline(average,linewidth=4, color='g', label = "Среднее изначальное")
    plt.legend()
    ax.grid()
    
    ax = fig.add_subplot(2,2,2)
    ax.set_title("Распределение стандартного отклонения")
    ax.hist(distribution_stde, 50, color = "lightblue", ec="red", edgecolor="black", rwidth = 5)
    plt.axvline(stde,linewidth=4, color='g', label = "Отклонение изначальное")
    plt.legend()
    ax.grid()

    ax = fig.add_subplot(2,1,2)
    ax.set_title("Выборка")
    plt.xticks(rotation="vertical")
    ax.plot(markers, data, '-bo', linewidth=2, markersize=6, markerfacecolor='black')
    plt.axhline(average + stde, color = "green")
    plt.axhline(average - stde, color = "green")
    plt.legend (('Факт', 'Тренд'))
    ax.grid()
    plt.savefig('result.png')
    plt.show()
'''
читаем данные
считаем исходные статистики
бутстрап и отрисовка на графиках
'''
read(data, markers)
average = statistics.mean(data)
stde = statistics.stdev(data)
bootstrap()
