import pandas as pd
import random
import statistics
import matplotlib.pyplot as plt

'''
простой перестановочный тест
метод грубой силы
!!! Перепиши этот код, это код не мужа, а мальчика

1) считаем разницу средних между изначальными группами
2) сливаем группы в один пул
3) делаем 10.000 выборок без возврата из этого пула в две новые группы
4) считаем разницу между выборочными статистиками
5) отрисовываем на графике и наносим туда же изначальную
6) чем дальше от основной массы находится изначальная статистика, тем больше вероятность, что
результаты в группах отличаются и отличаются не случайно
!!!!нет оценки p значения и не задается доверительный интервал а
!!!Также группы должны быть одинаковы - предусмотреть иной вариант
'''


def choose(count_elems, data):
    choosen = []
    i = 0
    index = 0
    while i < count_elems:
        index = random.randint(0,len(data)-1)
        choosen.append(data[index])
        data.remove(data[index])
        i+=1
    return choosen

def cop(data_old):
    data_new = []
    counter = 0
    while counter < len(data_old):
        data_new.append(data_old[counter])
        counter += 1
    return data_new

    

raw = pd.read_csv('1.csv', encoding = 'Windows-1251')
'''
считаем статистики в каждой из групп и находим их разницы
'''
mean_raw = raw['Группа 1'].mean() - raw['Группа 2'].mean()
'''
слитые в один массив группы
'''
common_groups = []
mean_ch = []

'''
Объединяем группы в один пул
'''
counter = 0
while counter < len(raw['Группа 1']):
        common_groups.append(raw['Группа 1'][counter])
        counter += 1
counter = 0
while counter < len(raw['Группа 2']):
        common_groups.append(raw['Группа 2'][counter])
        counter += 1

'''
делаем 10.000 выборок без возврата в новые группы, считаем разницу средних
и записываем в mean_ch
'''
counter = 0
while counter < 10000:
    data_tmp = cop(common_groups)
    g1 = choose(len(raw['Группа 1']), data_tmp)
    g2 = choose(len(raw['Группа 2']), data_tmp)
    mean_ch.append(statistics.mean(g1) - statistics.mean(g2))
    counter += 1

'''
отрисовываем распределение и наносим  разницу изначальных статистик
визуально оцениваем есть ли различия
'''
fig, ax = plt.subplots(figsize=(25,10))
ax.hist(mean_ch,bins=30, linewidth=2, color = 'green', edgecolor="black", rwidth = 5)
plt.axvline(mean_raw,linewidth=4, color='r', label = "Статистика изначальная")
plt.legend()
ax.grid()
plt.show()

