import math
import statistics

#что умеем:
#тестовый коммит =)
# среднее, медиана, дисперсия, стандартное отклонение, коэффициент вариации выборки
# расчет границ интервалов по формуле Стерджесса и разбивка на интервалы
# проверка разбиения на корректность с помощью коэффициента вариации
# считает среднее усеченное(отсекает мин и макс и считает среднее)
#

#графическое распределение значений изначальной выборки и на каждом шаге отсечения

result1 = []
list1 = []
inf = open('input.txt', 'r')
for item in inf:
        result1.append(item)
        
list1 = [float(item) for item in result1]
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

print("Исходные данные: ")
print(list1)
print("отсортированные данные: ")
print(list_sorted)
print("среднее: ")
print(average)
print("среднее усеченное(без минимум и максимум)")
print(average_short)
print("медиана: ")
print(median)
print("стандартное отклонение: ")
print(stde)
print("коэффициент вариации: ")
print(varia)
print("граница интервала: ")
print(interv)
print("число интервалов: ")
print(k)

#принцип действия:
#задаем нижнюю и верхнюю границы очередного интервала
# ищем все элементы, которые подпадают под интервал
# когда элементы кончаются, переходим к следующему интервалу
#исходный массив переписываем в список групп с индексом [0][n]
# где n - число групп

a1 = []
border_max = min1 + interv
border_min = min1
groups = 0
while groups < k:
    a2 = []
    for elems in list1:
        if(elems <= border_max and elems > border_min):
            a2.append(elems)
    groups = groups + 1
    border_min = border_max
    border_max = border_max + interv
    a1.append(a2)

# вывод групп и проверка на коэффициенты вариации
print("получились группы")
elems = 0
while elems < k:
    print(a1[elems])
    elems = elems + 1

print("их коэффициенты вариации: ")
elems = 0
while elems < k:
    if len(a1[elems]) > 1:
        stde1 = statistics.stdev(a1[elems])
        average1 = statistics.mean(a1[elems])
        varia1 = stde1 / average1
        print(varia1)
    else: 
        print("0")
    elems = elems + 1
#######################################################
    


