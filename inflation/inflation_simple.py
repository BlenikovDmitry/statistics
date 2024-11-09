import csv
import matplotlib.pyplot as plt

def top_elems(delta, position):
    max_elem = 0
    position_max_elem = 0
    index_max_elem = 0
    counter = 0
    copy_position = []
    copy_delta = []
    while counter < len(delta):
        copy_position.append(position[counter])
        copy_delta.append(delta[counter])
        counter += 1
    counter_upper = 0
    counter = 0
    while counter_upper < MAX_ELEMS_TOP:
        counter = 0
        max_elem = 0
        while counter < len(copy_delta):
            if max_elem < copy_delta[counter]:
                max_elem = copy_delta[counter]
                position_max_elem = counter
            counter += 1
        position_top.append(copy_position[position_max_elem])
        delta_top.append(max_elem)
        copy_position.pop(position_max_elem)
        copy_delta.remove(copy_delta[position_max_elem])
        counter_upper += 1
    

"""
Простейший скрипт подсчета инфляции
Вход: файл input_simple.csv
Содержит категории трат и суммы затрат по годам(текущий и предыдущий) по каждой категории 
Вывод:
"""
#категория
position = []
#затраты на начало наблюдений
price_old = []
#затраты на конец наблюдений
price_new = []
#разрыв между элементами круговой диаграммы
explode = []
#разница затрат между было и стало
delta = []
#категории с самой высоким ростом
position_top = []
#рост в категориях с самыс высоким ростом
delta_top = []
#число отбираемых топовых категорий
MAX_ELEMS_TOP = 6
"""
чтение данных в структуры данных
"""
with open('input_simple.csv', 'r', newline='') as csvfile:
    data_reader = csv.reader(csvfile, delimiter=',')
    for row in data_reader:
        position.append(row[0])
        price_old.append(float(row[1]))
        price_new.append(float(row[2]))
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
print("Инфляция по всем позициям составила : " + str(infl) + "%")
"""
//////////////////////////////////////////////////
"""
"""
построение графиков по долям в расходах и инфляции по категориям
"""
price_new.pop(0)
price_old.pop(0)
position.pop(0)
counter = 0.7
for row in position:
    explode.append(float(1-counter))
    counter += 0.01
    
plt.subplot(2, 2, 1)
plt.title("Структура потребления была")
plt.pie(price_old, labels=position, explode=explode, autopct='%1.1f%%',
        wedgeprops={'lw':1, 'ls':'--','edgecolor':"k"})
plt.axis("equal")

plt.subplot(2, 2, 2)
plt.title("Структура потребления сейчас")
plt.pie(price_new, labels=position, explode=explode, autopct='%1.1f%%',
        wedgeprops={'lw':1, 'ls':'--','edgecolor':"k"})
plt.axis("equal")


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

plt.subplot(2, 2, 3)
plt.bar(position, delta, color = colors, ec='black',linewidth = 2)
plt.grid()
plt.xticks(rotation=90)
plt.title('Инфляция по всем позициям(%)')
"""
Считаем MAX_ELEMS_TOP категории с наиболее высоким уровнем инфляции
"""
top_elems(delta,position)
print(str(MAX_ELEMS_TOP) + " позиций с самым высоким ростом затрат:")
print(position_top)
"""
///////////////////////////////////
"""
"""
Считаем MAX_ELEMS_TOP категории с наиболее высокими затратами на конец наблюдений
"""
position_top.clear()
delta_top.clear()
top_elems(price_new,position)
print(str(MAX_ELEMS_TOP) + " самых важных по затратам позиций:")
print(position_top)
"""
/////////////////////////////////////
"""
"""
Расчет инфляции по самым крупным позициям и вывод графика по ним
"""
counter = 0
counter_upper = 0
delta_t = []
colors.clear()
while counter_upper < len(position_top):
    counter = 0
    while counter < len(position):
        if position_top[counter_upper] == position[counter]:
            delta_t.append(delta[counter])
            if delta[counter] < 0:
                colors.append('red')
            if delta[counter] >= 0:
                colors.append('blue')
        counter += 1
    counter_upper += 1
plt.subplot(2, 2, 4)
plt.bar(position_top, delta_t, color = colors, ec='black',linewidth = 2)
plt.grid()
plt.xticks(rotation=90)
plt.title('Инфляция по топ позициям(%)')

    
sum_price_old = 0
sum_price_new = 0
counter = 0
counter_upper = 0
while counter_upper < len(position_top):
    counter = 0
    while counter < len(price_old):
        if position_top[counter_upper] == position[counter]:
            sum_price_old += float(price_old[counter])
            sum_price_new += float(price_new[counter])
        counter += 1
    counter_upper += 1

infl = sum_price_new / sum_price_old * 100 - 100
infl = round(infl, 2)

print("Инфляция по самым крупным позициям: " + str(infl) + "%")

"""
///////////////////////////////////////////
"""
plt.show()



