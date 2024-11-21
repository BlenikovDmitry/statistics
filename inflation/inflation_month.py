import csv
import matplotlib.pyplot as plt
import statistics


#месяц
month = []
#затраты
cost = []
#помесячная инфляция
infl_perc_month = []
#финальная инфляция
infl_total = 0

"""
Простейший скрипт подcчета помесячной инфляции
Вход: файл input_month.csv
Содержит столбец с месяцами и столбец с затратами в рублях
Вывод: в консоль среднее, медиану, стандартное отклонение
В отдельное окно график затрат в рублях
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
Подсчет инфляции в процентах помесячной
Подсчет накопленно инфляции
Подсчет среднего, медианы и страндартного отклонения
"""
counter = 1
infl_perc_month.append(0.0)
while counter < len(cost):
    infl_perc_month.append(round((cost[counter] / cost[counter - 1] - 1),2))
    counter += 1

#накопленная считается так: (1 + инфл январь) * (1 + инфл февраль) * и тд
# инфляция должна быть в долях, а не процентах, те 0.05 а не 5%
infl_total = 1
for elem in infl_perc_month:
    infl_total *= (1+ elem)
infl_total -= 1

print("Рост затрат за период составил: ", str(round((infl_total * 100), 2)) + "%")
print("Средняя: ", str(round((statistics.mean(cost) / cost[0] - 1) * 100, 2)) + "%")
print("Медиана: ", str(round((statistics.median(cost) / cost[0] - 1) * 100, 2)) + "%")
print("Отклонение: ", str(round(statistics.pstdev(cost), 2)) + "%")
print(infl_perc_month)
"""
///////////////////////////////////////////////////
"""

"""
отрисовка графика
"""
fig, ax = plt.subplots()
plt.title('Динамика затрат по месяцам в рублях')
plt.xlabel("Месяц")
plt.ylabel("Затраты(руб)")
ax.plot(month, cost, 'o-', linewidth=2.0, color = 'red', markeredgecolor='black',
        markerfacecolor='blue')

ax.grid()
plt.show()
"""
////////////////////////////////////////////////////
"""

