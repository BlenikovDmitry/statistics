import math
import statistics
import matplotlib.pyplot as plt
import csv
import random

#простейший скрипт бутстраппирования
#умеет:
#читает файл .csv
#делает 10.000 случайных выборок с возвратом
#считает среднее, медиану, стандартное отклонение


#построить несколько графиков распределений: среднее, стандартное отклонение

#спискм маркеров и элементов генеральной совокупности
markers = []
data = []
#считываем из файла .csv входные данные
with open("in.csv", 'r') as f:
        reader = csv.reader(f)
        for row in reader:
                markers.append(str(row[0]))
                data.append(float(row[1]))
print("Вычисления начались")
#вспомогательные списки маркеров и выборки
markers_var = []
data_var = []

counter_iteration = 0
counter = 0
tmp = 0
distribution_average = []
distribution_median = []
distribution_stde = []
while counter_iteration < 10000:
        counter = 0
        markers_var = []
        data_var = []
        while counter < len(markers):
                tmp = random.random() * len(data)
                data_var.append(data[int(tmp)])
                markers_var.append(markers[int(tmp)])
                counter = counter + 1

        # среднее
        average = statistics.mean(data_var)
        #медиана
        median = statistics.median(data_var)
        #стандартное отклонение
        stde = statistics.stdev(data_var)
       # result = ["Среднее", str(average), "Медиана", median, "Стандартное отклонение", stde]
        distribution_average.append(average)
        distribution_median.append(median)
        distribution_stde.append(stde)
        #with open('result.csv', 'a') as f:
         #       writer = csv.writer(f,  lineterminator='\n')
         #       writer.writerow(result)
        
        counter_iteration = counter_iteration + 1
print("Вычисления окончены")
fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot(2,2,1)
ax.set_title("Распределение среднего")
ax.hist(distribution_average, 50, color = "red", ec="red")
ax.grid()

ax1 = fig.add_subplot(2,2,3)
ax1.set_title("Распределение медианы")
ax1.hist(distribution_median, 50, color = "green", ec="red")
ax1.grid()

ax2 = fig.add_subplot(1,2,2)
ax2.set_title("Распределение стандартного отклонения")
ax2.hist(distribution_stde, 50, color = "lightblue", ec="red")
ax2.grid()


plt.show()


