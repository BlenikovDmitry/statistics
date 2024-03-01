import random

"""
Функция потерь
попарно берет разницу между значениями, возводит в квадрат и берет среднее
Так мы узнаем, насколько сильно различаются прогнозные и фактические данные

!!!ВАЖНО размер выборок должен быть одинаков и обе выборки должны быть порождены одним процессом
Иначе в функции нет смысла
Подаем на вход:
- plan - прогнозный результат
- fact - фактический результат

Возвращает среднее - насколько различаются выборки

"""
def lost_function(plan, fact):
    diff = 0
    average = 0
    counter = 0
    
    while counter < len(plan):
        diff = plan[counter] - fact[counter]
        diff = diff * diff
        average = average + diff
        counter = counter + 1
    average = average / len(plan)
    
    return average

#Функция выборки с возвратом
#Берет данные и маркеры из генеральной совокупности
#в случайном порядке
# передаем на вход:
# data - генеральная совокупность
# markers - маркеры(дата, время, категории, хоть черт лысый)
# data_var - сюда пишем выборку
# markers_var - сюда пишем выборку маркеров
# ничего не возвращает, нужно использовать глобальные массивы для результата
def selection_with_return_markers(data, markers, data_var, markers_var):
    counter = 0
    tmp = 0
    while counter < len(markers):
        tmp = random.random() * len(data)
        data_var.append(data[int(tmp)])
        markers_var.append(markers[int(tmp)])
        counter = counter + 1
        
#Функция выборки с возвратом
#Берет данные и маркеры из генеральной совокупности
#в случайном порядке
# передаем на вход:
# data - генеральная совокупность
# data_var - сюда пишем выборку
# возвращает массив data_var  с результатами
def selection_with_return_without_markers(data):
    data_var = []
    counter = 0
    tmp = 0
    while counter < len(markers):
        tmp = random.random() * len(data)
        data_var.append(data[int(tmp)])
        counter = counter + 1
    return data_var

#Функция выборки без возврата
#Берет данные и маркеры из генеральной совокупности
#в случайном порядке
# передаем на вход:
# data - генеральная совокупность
# markers - маркеры(дата, время, категории, хоть черт лысый)
# data_var - сюда пишем выборку
# markers_var - сюда пишем выборку маркеров
# elems - сколько элементов должно быть в выборке, если элементов в выборке больше чем есть в генеральной совокупности, вернет 0
# ничего не возвращает, нужно использовать глобальные массивы для результата!!!!!изменяет исходные массивы
def selection_without_return_markers(data, markers, data_var, markers_var, elems):
    if elems > len(markers):
        return 0
    counter = 0
    tmp = 0
    while counter < elems:
        tmp = random.random() * len(data)
        data_var.append(data[int(tmp)])
        markers_var.append(markers[int(tmp)])
        data.remove(data[int(tmp)])
        markers.remove(markers[int(tmp)])
        counter = counter + 1

#Функция выборки без возврата
#Берет данные и маркеры из генеральной совокупности
#в случайном порядке
# передаем на вход:
# data - генеральная совокупность
# data_var - сюда пишем выборку
# elems - сколько элементов должно быть в выборке, если элементов в выборке больше чем есть в генеральной совокупности, вернет 0
# ничего не возвращает, нужно использовать глобальные массивы для результата!!!!!изменяет исходные массивы
def selection_without_return_without_markers(data, data_var, elems):
    if elems > len(data):
        return 0
    counter = 0
    tmp = 0
    while counter < elems:
        tmp = random.random() * len(data)
        data_var.append(data[int(tmp)])
        data.remove(data[int(tmp)])
        counter = counter + 1

"""
Копирует один массив в другой
"""
def memcpy(data_old,data_new):
    for elems in data_old:
        data_new.append(elems)
"""
Подсчитывает суммы повторно выбранных групп
для проверки статистической гипотезы о случайности значений в группах
"""
def selection_groups_sel_statictics(data, data_all):
    data_var = []
    data_tmp = []
    sums_tmp = []
    sums = 0
    counter = 0
    while counter < len(data):
        memcpy(data_all, data_var)
        selection_without_return_without_markers(data_var, data_tmp, len(data[counter]))
        for elem in data_tmp:
            sums = sums + float(elem)
        sums_tmp.append(sums)
        counter = counter + 1
        sums = 0
        data_tmp = []
        data_var = []
    return sums_tmp

"""
считывает данные из файла in.csv
записывает в два массива:
- markers - маркеры
- data - данные
"""
def read(data, markers):
    with open("in.csv", 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            markers.append(str(row[0]))
            data.append(float(row[1]))
"""
Бутстрап
делает 10.000 итераций , формирует распределение среднего, медианы, стандартного отклонения
отрисовывает распределение среднего, стандартного отклонения, выборку
"""
def bootstrap(data, markers):
    counter_iteration = 0
    counter = 0
    tmp = 0
    distribution_average = []
    distribution_median = []
    distribution_stde = []
    while counter_iteration < 10000:
        counter = 0
        markers_var = []
        data_var = []
        while counter < len(markers):
            tmp = random.random() * len(data)
            data_var.append(data[int(tmp)])
            markers_var.append(markers[int(tmp)])
            counter = counter + 1

      
        average = statistics.mean(data_var)
    
        median = statistics.median(data_var)
 
        stde = statistics.stdev(data_var)
       
        distribution_average.append(average)
        distribution_median.append(median)
        distribution_stde.append(stde)
    
        
        counter_iteration = counter_iteration + 1
    fig = plt.figure(figsize=(6,6))
    ax = fig.add_subplot(2,2,1)
    ax.set_title("Распределение среднего")
    ax.hist(distribution_average, 50, color = "red", ec="red")
    ax.grid()
    
    ax = fig.add_subplot(2,2,2)
    ax.set_title("Распределение стандартного отклонения")
    ax.hist(distribution_stde, 50, color = "lightblue", ec="red")
    ax.grid()

    ax = fig.add_subplot(2,2,3)
    ax.set_title("Выборка")
    ax.plot(markers, data, color = "lightblue")
    ax.grid()

    plt.show()
