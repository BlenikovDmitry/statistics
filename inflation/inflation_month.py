import csv
import matplotlib.pyplot as plt
import statistics


#месяц
month = []
#затраты
cost = []
#помесячная инфляция
infl_perc_month = []
#общая инфляция за весь период
infl_total = 0
"""
Простейший скрипт подcчета помесячной инфляции
Вход: файл input_month.csv
Содержит столбец с месяцами и столбец с затратами в процентах
Вывод: в консоль общую инфляцию за период, среднее, стандартное отклонение
В отдельное окно динамика затрат в %
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
infl_perc_month.append(0.0)
while counter < len(cost):
    infl_perc_month.append(round((cost[counter] / cost[counter - 1] - 1),2))
    counter += 1


counter = 0
sum_was = 0
sum_is = 0
while counter < len(cost):
    sum_was += cost[0]
    sum_is += cost[counter]
    counter += 1

infl_total = (sum_is / sum_was) * 100 - 100
dev = round(statistics.pstdev(infl_perc_month), 2)
print(sum_was)
print(sum_is)
print("Общий рост расходов за период: ", str(round(infl_total, 2)) + "%")
print("Средняя динамика по месяцам: ", str(round(statistics.mean(infl_perc_month), 2)) + "%")
print("Отклонение: ", str(dev) + "%")
print(infl_perc_month)
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
#ax.plot(month, infl_perc_month, 'o-', linewidth=2.0, color = 'red', markeredgecolor='black', markerfacecolor='blue', label = 'динамика затрат')
#отрисовка линий стандартного отклонения
#ax.axhline(dev, linewidth=2, color='b')
#ax.axhline((dev * (-1)), linewidth=2, color='b', label = 'Границы нормальности')
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


