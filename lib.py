import random

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


def memcpy(data_old,data_new):
    for elems in data_old:
        data_new.append(elems)

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
