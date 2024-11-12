import matplotlib.pyplot as plt
import csv
import statistics

"""
Скрипт считает распределение доходностей в облигациях, строит гистограмму
Также делает простейший анализ(считает среднее ,медиану ,моду), чтобы показать , около каких значений группировка доходностей
Для входа нужен файл .csv формата
<название> <код> <число бумаг> <купонная доходность>
купонная доходность уже должна быть приведена к цене покупки в портфель

Принцип действия:
- считываем данные
- считаем центральное положение
- строим гистограмму

"""
bonds_count = []
percents_coupon = []
"""
чтение данных в структуры данных
"""
with open('russian_bonds.csv', 'r', newline='') as csvfile:
    data_reader = csv.reader(csvfile, delimiter=';')
    for row in data_reader:
        bonds_count.append(str(row[2]))
        percents_coupon.append(str(row[3]))
"""
////////////////////////////////////////////////////
"""
bonds_count.pop(0)
percents_coupon.pop(0)

counter = 0
while counter < len(bonds_count):
    bonds_count[counter] = int(bonds_count[counter])
    percents_coupon[counter] = float(percents_coupon[counter])
    counter += 1

result = []
counter_upper = 0
counter = 0

while counter_upper < len(bonds_count):
    counter = 0
    while counter < bonds_count[counter_upper]:
        result.append(percents_coupon[counter_upper])
        counter += 1
    counter_upper += 1

print("среднее:" + str(statistics.mean(percents_coupon)))
print("медиана:" + str(statistics.mode(percents_coupon)))
print("мода:" + str(statistics.median(percents_coupon)))

fig, ax = plt.subplots()
plt.title("Распределение купонов")
plt.xlabel("Купонная доходность")
plt.ylabel("Число купленных бумаг")
ax.hist(result, bins=len(bonds_count), linewidth=2, color = 'green', edgecolor="black", rwidth = 5)
ax.grid()
plt.show()
