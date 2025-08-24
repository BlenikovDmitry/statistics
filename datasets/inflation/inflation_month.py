import csv
import matplotlib.pyplot as plt
import statistics


#месяц
month = []
#затраты
cost = []
#помесячная инфляция относительно предыдущего месяца
infl_perc_month = []
#помесячная инфляция относительно стартовой точки
#infl_perc_month_abs = []
#общая инфляция за весь период
infl_total = 0
"""
Простейший скрипт подcчета помесячной инфляции
Вход: файл input_month.csv
Содержит столбец с месяцами и столбец с затратами в процентах
Первой строчкой важно указать стартовую точку(название любое, сумма, от которой отталкиваемся)
Вывод: в консоль общую инфляцию за период, среднее, стандартное отклонение
В отдельное окно динамика затрат в %
!!!Написан работающий код для подсчета инфляции относительно стартовой точки, но он закомментирован
"""


"""
чтение данных в структуры данных
"""
with open('input_month.csv', 'r', newline='') as csvfile:
    data_reader = csv.reader(csvfile, delimiter=';')
    for row in data_reader:
        month.append(row[0])
        cost.append(float(row[1]))
"""
////////////////////////////////////////////////////
"""
"""
Подсчет инфляции за весь период
Подсчет инфляции в процентах помесячной
Подсчет среднего и страндартного отклонения
"""

counter = 1
while counter < len(cost):
    infl_perc_month.append(round((cost[counter] / cost[counter - 1] - 1),2))
    #infl_perc_month_abs.append(round((cost[counter] / cost[0] - 1),2))
    counter += 1

#start_point = cost[0]
cost.pop(0)
month.pop(0)

counter = 0
sum_was = 0
sum_is = 0
while counter < len(cost):
    sum_was += cost[0]
    sum_is += cost[counter]
    counter += 1

infl_total = (sum_is / sum_was) * 100 - 100
dev = round(statistics.pstdev(infl_perc_month), 2)
print("Общий рост расходов за период: ", str(round(infl_total, 2)) + "%")
print("Средняя динамика по месяцам: ", str(round(statistics.mean(infl_perc_month), 2)) + "%")
print("Отклонение: ", str(dev) + "%")
print(infl_perc_month)
print(sum(infl_perc_month))
#print(infl_perc_month_abs)
#print(sum(infl_perc_month_abs))
"""
///////////////////////////////////////////////////
"""

"""
отрисовка графика всех данных
"""
fig, ax = plt.subplots()
plt.title('Динамика затрат по месяцам')
plt.xlabel("Месяц")
plt.ylabel("Затраты(рост/падение) %")

counter = 0
colors = []
while counter < len(infl_perc_month):
    if infl_perc_month[counter] < 0:
        colors.append('red')
    if infl_perc_month[counter] >= 0:
        colors.append('blue')
    counter += 1

bars = []
bars = ax.bar(month, infl_perc_month, color = colors, edgecolor="black")
ax.axhline(dev, linewidth=2, color='black')
ax.axhline((dev * (-1)), linewidth=2, color='black', label = 'Границы нормальности')

ax.bar_label(bars)

ax.grid()
ax.legend()
plt.show()
"""
////////////////////////////////////////////////////
"""


