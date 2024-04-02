import math
import statistics
import matplotlib.pyplot as plt
import csv
import random

#что умеем:
# среднее, медиана, дисперсия, стандартное отклонение, коэффициент вариации выборки
# расчет границ интервалов по формуле Стерджесса и разбивка на интервалы
# проверка разбиения на корректность с помощью коэффициента вариации
# считает среднее усеченное(отсекает мин и макс и считает среднее)
# читает и пишет в файл csv
# строит график распределения величин
# наносит среднее, медиану, задает границы нормального распределения(правило сигм)
#считает сколько точек попало в границы сигм(стандартных отклонений)
#считает, сколько % точек лежит внутри сигма1 и сигма2
#считает диапазон сигмы1 и сигмы2
#

markers = []
markers1 = []
result = []
list1 = []
counter = 0
#считываем маркеры и сами данные
with open("in.csv", 'r') as f:
        reader = csv.reader(f)
        for row in reader:
                markers1.append(str(row[0]))
                list1.append(float(row[1]))

#сортируем выборку
list_sorted = sorted(list1)

#рассчитываем стандартные статистики
# среднее
average = statistics.mean(list1)
#медиана
median = statistics.median(list1)
#дисперсия
disp = statistics.pvariance(list1)
#стандартное отклонение
stde = statistics.stdev(list1)
#коэффициент вариации
varia = stde / average
#максимум и минимум всей выбоки
max1 = max(list1)
min1 = min(list1)
#среднее усеченное(отсекаем мин и макс из изначальной выборки)
list_sorted1 = sorted(list1)
list_sorted1.remove(max1)
list_sorted1.remove(min1)
average_short = statistics.mean(list_sorted1)
########################################################
## расчет границы интервалов, количества интервалов ####
## и разбивка на интервалы по Стерджессу ###############
# считаем вернхнюю границу интервала
interv = (max1 - min1) / (1 + math.log2(len(list1)))
#считаем число интервалов
k = (max1 - min1) / interv

k = math.ceil(k)
interv = math.ceil(interv)
        
    
#принцип действия:
#задаем нижнюю и верхнюю границы очередного интервала
# ищем все элементы, которые подпадают под интервал
# когда элементы кончаются, переходим к следующему интервалу
#исходный массив переписываем в список групп с индексом [0][n]
# где n - число групп
groups_info = []
a1 = []
border_max = min1 + interv
border_min = min1
groups = 0
while groups <= k:
    a2 = []
    for elems in list1:
        if(elems < border_max and elems >= border_min):
            a2.append(elems)
    groups = groups + 1
    border_min = border_max
    border_max = border_max + interv
    a1.append(a2)
    if a2:
            group_min = min(a2)
            group_max = max(a2)
            group_count = len(a2)
            groups_info.append("("+str(group_min) + "-" + str(group_max)+ ")" + " к-во: " + str(group_count))


elems = 0
while elems < k:
    elems = elems + 1

elems = 0
result_varia = []
while elems < k:
        if len(a1[elems]) > 1:
                stde1 = statistics.stdev(a1[elems])
                average1 = statistics.mean(a1[elems])
                varia1 = stde1 / average1
                result_varia.append(round(varia1, 2))
        else: 
                result_varia.append("0")
        
        elems = elems + 1
#######################################################
#считает сколько точек попало в границы сигм(стандартных отклонений)
#считает, сколько % точек лежит внутри сигма1 и сигма2
#считает диапазон сигмы1 и сигмы2
#######################################################
count_sigma1 = 0
count_sigma2 = 0
count_sigma1_perc = 0
count_sigma2_perc = 0
min_sigma1 = 100000
max_sigma1 = 0
min_sigma2 = 100000
max_sigma2 = 0
for elem in list1:
        if(int(elem >= (average - stde)) & int(elem <= (average + stde))):
                count_sigma1 = count_sigma1 + 1
                if(elem < min_sigma1):
                        min_sigma1 = elem
                if(elem > max_sigma1):
                        max_sigma1 = elem
        if(int(elem >= (average - stde * 2)) & int(elem <= (average + stde * 2))):
                count_sigma2 = count_sigma2 + 1
                if(elem < min_sigma2):
                        min_sigma2 = elem
                if(elem > max_sigma2):
                        max_sigma2 = elem

count_sigma1_perc = count_sigma1 / int(len(list1)) * 100
count_sigma2_perc = count_sigma2 / int(len(list1)) * 100
#######################################################
#Формирование выходных данных
result_data = ["Исходные данные: "]
result_data1 = ["Маркеры"]
result_statistics_average = ["Среднее", average]
result_statistics_average_short = ["Cреднее усеченное(без минимума и максимума):",average_short]
result_statistics_median = ["Медиана:", round(median, 2)]
result_statistics_stde = ["Стандартное отклонение:", round(stde, 2)]
result_statistics_varia = ["Коэффициент вариации:", round(varia, 2)]
result_statistics_interv = ["Граница интервала:", round(interv, 2)]
result_statistics_intervals_number = ["Число интервалов:", k]
result_groups = ["Получились группы:"]
result_groups_varias = ["Их коэффициенты вариации:"]
result_sigma = ["Точек в границах стандартного отклонения", str(len(list1))]
result_sigma1 = ["Точек в границах стандартного отклонения(абсолютное, относительное, диапазон)", str(count_sigma1), str(count_sigma1_perc),
                 str(min_sigma1) + "-" + str(max_sigma1)]
result_sigma2 = ["Точек в границах 2 стандартных отклонений(абсолютное, относительное, диапазон)", str(count_sigma2), str(count_sigma2_perc),
                 str(min_sigma2) + "-" + str(max_sigma2)]
##############################################################

# вывод результатов а файл и проверка на коэффициенты вариации
with open('result.csv', 'w') as f:
    writer = csv.writer(f,  lineterminator='\n')
    writer.writerow(result_statistics_average)
    writer.writerow(result_statistics_average_short)
    writer.writerow(result_statistics_median)
    writer.writerow(result_statistics_stde)
    writer.writerow(result_statistics_varia)
    writer.writerow(result_statistics_interv)
    writer.writerow(result_statistics_intervals_number)
    writer.writerow(result_groups + groups_info)
    writer.writerow(result_groups_varias + result_varia)
    writer.writerow(result_sigma)
    writer.writerow(result_sigma1)
    writer.writerow(result_sigma2)
    

print("Выборка исследована, результаты в файле")
#######################################################
plt.figure(figsize=(15,15))
plt.title("Распределение значений")
plt.xlabel("Маркеры")
plt.ylabel("Значения")
plt.scatter(markers1, list1,color = 'red', marker = 'o')
plt.axhline(average, color = 'blue', label = 'Среднее')
plt.axhline(median, color = 'green', label = 'Медиана')
plt.axhline(average + stde, color = 'black', label ='Первая сигма(>= 68%)', linewidth = 5)
plt.axhline(average - stde, color = 'black', linewidth = 5)

plt.axhline(average + stde * 2, color = 'orange', label ='Вторая сигма(>= 95%)', linewidth = 5)
plt.axhline(average - stde * 2, color = 'orange', linewidth = 5)

plt.legend()
plt.show()






