import math
import statistics
import matplotlib.pyplot as plt
import csv
import random
import lib

#сюда читаем данные из файла построчно
data = []
#сюда пишем объединенные данные
data_all = []

with open("in.csv", 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            data.append(row)

#очищаем данные от пустых значений и подсчитываем разность исходных групп
counter = 0
while counter < len(data):
    data[counter] = [i for i in data[counter] if i]
    counter = counter + 1
####################################################
    
#объединяем группы в одну
for elem in data:
    data_all = data_all + elem
    counter = 0
##################################

#рассчитываем эталонную статистику
counter = 0
sums = 0
stats_etalon = 0
data_stats = []
for elem in data:
        while counter < len(elem):
                sums = sums + float(elem[counter])
                counter = counter + 1
        data_stats.append(sums)
        sums = 0
        counter = 0

stats_etalon = data_stats[0]
counter = 1
while counter < len(data_stats):
        stats_etalon = stats_etalon - float(data_stats[counter])
        counter = counter + 1
##################################################################
#создаем копию исходных данных объединенных для расчетов

counter = 0
stats_buts = []
while counter < 10000:
        stats = 0
        sums_tmp = []
        sums_tmp = lib.selection_groups_sel_statictics(data, data_all)
        stats = sums_tmp[0]
        counter1 = 1
        while counter1 < len(sums_tmp):
                stats = stats - sums_tmp[counter1]
                counter1 = counter1 + 1
        stats_buts.append(stats)    
        counter = counter + 1

print(stats_etalon)
fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot()
ax.set_title("Распределение выборочной разницы")
ax.hist(stats_buts, 50, color = "red", ec="black")
plt.axvline(stats_etalon, linewidth = 5, color = "green")
ax.grid()
plt.show()
