import math
import statistics
import matplotlib.pyplot as plt
import csv
import random

"""
Анализ исторических значений
Рассчитываем среднее, медиану ,стандартное отклонение

Бутстрапируем полученную выборку, отрисовываем распределение среднего и
стандартного отклонения(10.000 итераций)

Отрисовываем график из 2 кривых:
1 - фактическая выборка после фильтрации
2 - прогнозная - среднее значение от 1 до n, где n - текущий элемент итерации

!!!ВАЖНО
Хорошо работает на выборках, которые имеют ограниченный диапазон значений
Если диапазон широк, то может только показать общий тренд


"""


data = []
markers = []
data_eject = []
markers_eject = []
data_result = []
markers_result = []
average = 0
median = 0
stde = 0
def read(data, markers):
    with open("in.csv", 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            markers.append(str(row[0]))
            data.append(float(row[1]))
        
        

def bootstrap(data, markers, data_result):
    counter_iteration = 0
    counter = 0
    tmp = 0
    distribution_average = []
    distribution_median = []
    distribution_stde = []
    lost_function_results = []
    while counter_iteration < 10000:
        counter = 0
        markers_var = []
        data_var = []
        while counter < len(data):
            tmp = random.random() * len(data)
            data_var.append(data[int(tmp)])
            counter = counter + 1

      
        average = statistics.mean(data_var)
    
        median = statistics.median(data_var)
 
        stde = statistics.stdev(data_var)
       
        distribution_average.append(average)
        distribution_median.append(median)
        distribution_stde.append(stde)
    
        
        counter_iteration = counter_iteration + 1
     
    fig = plt.figure(figsize=(6,6))
    ax = fig.add_subplot(2,2,1)
    ax.set_title("Распределение среднего")
    ax.hist(distribution_average, 50, color = "red", ec="lightblue", edgecolor="black", rwidth = 5)
    ax.grid()
    
    ax = fig.add_subplot(2,2,2)
    ax.set_title("Распределение стандартного отклонения")
    ax.hist(distribution_stde, 50, color = "lightblue", ec="red", edgecolor="black", rwidth = 5)
    ax.grid()


    average_average = statistics.mean(distribution_average)
    average_stde = statistics.mean(distribution_stde)
    print(average_average)
    print(average_stde)
    ax = fig.add_subplot(2,1,2)
    ax.set_title("Выборка")
    plt.xticks(rotation="vertical")
    ax.plot(markers, data, '-bo', linewidth=2, markersize=6, markerfacecolor='black')
    plt.axhline(average_average + average_stde, color = "green")
    plt.axhline(average_average - average_stde, color = "green")
    plt.legend (('Факт', 'Возможный коридор'))
    ax.grid()

    plt.show()

def prognozis(data, markers, data_result):
    counter = 1
    counter1 = 0
    average = 0
    data_result.append(data[0])
    while counter < len(data):
        counter1 = 0
        average = 0
        while counter1 < counter:
            average = average + data[counter1]
            counter1 = counter1 + 1
        average = average / counter
        data_result.append(average)
        counter = counter + 1

read(data, markers)

average = statistics.mean(data)
median = statistics.median(data)
stde = statistics.stdev(data)



min1 = 0
max1 = 0
index = 0


bootstrap(data, markers, data_result)








