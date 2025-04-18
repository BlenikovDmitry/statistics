import matplotlib.pyplot as plt
import csv
import statistics
import gc

"""
Скрипт считает распределение доходностей в облигациях относительно цены покупки, строит гистограмму
Также делает простейший анализ(считает среднее ,медиану ,моду, стандартное отклонение), чтобы показать , около каких значений группировка доходностей
Считает купонную доходность по выпускам и генерирует отдельный файл графика

Принцип действия:
- считываем данные
- считаем центральное положение
- строим гистограмму

"""
#название бумаги
bonds_name = []
#цена бумаги
bonds_price = []
#число бумаг
bonds_count = []
#номинал бумаги
nominal = []
#купон в рублях
coupon = []
#число выплат в год
coupon_count = []
"""
чтение данных в структуры данных
"""
with open('russian_bonds.csv', 'r', newline='',encoding="utf-8") as csvfile:
    data_reader = csv.reader(csvfile, delimiter=';')
    for row in data_reader:
        bonds_name.append(str(row[0]))
        bonds_price.append(str(row[1]))
        bonds_count.append(str(row[2]))
        nominal.append(str(row[3]))
        coupon.append(str(row[4]))
        coupon_count.append(str(row[5]))
#убираем заголовок
bonds_name.pop(0)
bonds_price.pop(0)
bonds_count.pop(0)
nominal.pop(0)
coupon.pop(0)
coupon_count.pop(0)


"""
////////////////////////////////////////////////////
"""

#делаем приведение типов и считаем цену покупки с учетом номинала и цены на бирже
counter = 0
while counter < len(bonds_count):
    bonds_count[counter] = int(bonds_count[counter])
    coupon_count[counter] = int(coupon_count[counter])
    coupon[counter] = float(coupon[counter])
    bonds_price[counter] = float(bonds_price[counter]) * int(nominal[counter]) / 100
    nominal[counter] = int(nominal[counter])
    counter += 1
#сюда собираем все купоны в % для анализа и отрисовки на гистограмму
result = []

#считаем купонные выплаты в % и заталкиваем в result
'''
Д - текущая доходность
Д = К / Ц * 100%, где:

К — сумма купонных выплат за период;
Ц — текущая рыночная цена облигации.
Подробнее на сайте Banki.ru https://www.banki.ru/news/daytheme/?id=10982360
в нашем случае:
К = coupon[counter_upper] * coupon_count[counter_upper](купон * число выплат в год)
Ц = bonds_price[counter_upper](цена бумаги на момент покупки с учетом рыночной цены в % поправленной на номинал покупки)
'''
counter_upper = 0
counter = 0
while counter_upper < len(bonds_count):
    counter = 0
    while counter < bonds_count[counter_upper]:
        result.append(((coupon[counter_upper] * coupon_count[counter_upper]) / bonds_price[counter_upper]) * 100)
        counter += 1
    counter_upper += 1
#центральное положение + стандартное отклонение
print("среднее:" + str(round(statistics.mean(result),2)) + '%')
print("медиана:" + str(round(statistics.mode(result),2)) + '%')
print("мода:" + str(round(statistics.median(result),2)) + '%')
print("Стандартное отклонение от среднего:" + str(round(statistics.stdev(result),2)) + '%')

#после анализа приводим к int, формируем шкалу по оси X и отрисовывааем на графике, сохраняя в отдельный файл
'''
отдельно генерируем доходности относительно цены покупки и распределение купонной доходности
'''
counter = 0
while counter < len(result):
    result[counter] = int(result[counter])
    counter += 1


x_ticks = []
counter = min(result)
while counter < max(result):
    x_ticks.append(counter)
    counter += 1

fig, ax = plt.subplots(figsize=(25,10))
plt.title("Распределение доходности")
plt.xlabel("Доходность")
plt.ylabel("Число купленных бумаг")
plt.xticks(x_ticks)

ax.hist(result,bins=len(bonds_name), linewidth=2, color = 'green', edgecolor="black", rwidth = 5)
plt.axvline(round(statistics.mean(result),2),linewidth=4, color='r', label = "Средний купон")
plt.legend()
ax.grid()
plt.savefig("interest_distribution.png")

del result
del counter_upper
gc.collect()

'''
(купон * число выплат в год / номинал * 100%
'''
counter = 0
interest = []
while counter < len(bonds_name):
    interest.append(round(coupon[counter] * coupon_count[counter] / nominal[counter] * 100,2))
    counter += 1


fig, ax = plt.subplots(figsize=(25,10))
plt.xticks(rotation="vertical")
ax.set_title("Распределение % купона по выпускам")
bars = ax.bar(bonds_name, interest, linewidth = 3.0, color = 'blue', ec='red')
ax.bar_label(bars)
ax.grid()
plt.savefig('coupon_distribution.png')
