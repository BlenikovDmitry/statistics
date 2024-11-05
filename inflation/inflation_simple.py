import csv
import matplotlib.pyplot as plt

"""
Простейший скрипт подсчета инфляции
Вход: файл input_simple.csv
Содержит категории трат и суммы затрат по годам(текущий и предыдущий) по каждой категории 
Вывод:
"""
position = []
price_old = []
price_new = []
"""
чтение данных в структуры данных
"""
with open('input_simple.csv', 'r', newline='') as csvfile:
    data_reader = csv.reader(csvfile, delimiter=',')
    for row in data_reader:
        position.append(row[0])
        price_old.append(row[1])
        price_new.append(row[2])
"""
////////////////////////////////////////////////////
"""
"""
подсчет общей инфляции
"""
sum_price_old = 0
sum_price_new = 0
counter = 1
while counter < len(price_old):
    sum_price_old += float(price_old[counter])
    sum_price_new += float(price_new[counter])
    counter += 1

infl = sum_price_new / sum_price_old * 100 - 100
infl = round(infl, 2)
print("Инфляция составила : " + str(infl) + "%")
"""
//////////////////////////////////////////////////
"""
"""
построение графиков по долям в расходах и инфляции по категориям
"""
price_new.pop(0)
price_old.pop(0)
position.pop(0)
explode = []
counter = 0.8
for row in position:
    explode.append(float(1-counter))
    counter += 0.02
    
plt.subplot(1, 2, 1)
plt.title("Структура потребления")
plt.pie(price_new, labels=position, explode=explode, autopct='%1.1f%%',
        wedgeprops={'lw':1, 'ls':'--','edgecolor':"k"})
plt.axis("equal")

delta = []
delta_tmp = 0
colors = []
counter = 0
while counter < len(price_new):
    delta_tmp = float(price_new[counter]) / float(price_old[counter]) * 100 - 100
    delta.append(delta_tmp)
    if delta_tmp < 0:
        colors.append('red')
    if delta_tmp >= 0:
        colors.append('blue')
        
        
    counter += 1

plt.subplot(1, 2, 2)
plt.bar(position, delta, color = colors, ec='black',linewidth = 2)
plt.grid()
plt.title('Инфляция по позициям(%)')

plt.show()


