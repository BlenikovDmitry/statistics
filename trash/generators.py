import sys
import psutil
import os
import gc

#генераторы списка и генераторы
#также делаем замер использования памяти утилитой psutil
#также идет работа с памятью, НО! после вызова сборщика мусора памяти используется
#больше, а потому что сборщик мусора не возвращает память ОС 

#генератор списка от 0 до 99
lst = [i for i in range(100)]
process = psutil.Process(os.getpid())
'''print('Использовано памяти в начале:')
print(process.memory_info().rss)'''
del lst
#генератор списка от 1 до 100
lst = [i for i in range(1, 100)]
del lst
#генератор списка квадраты чисел от 1 до 100
lst = [i **2 for i in range(1,100)]

gc.collect()

#Функция инкремента для примера
def incr(i):
    i += 1
    return i

#генерируем с помощью функции инкремента(для примера)
#Функция может быть любой
lst = [incr(i) for i in range(100)]
gc.collect()

#создаем объект генератора результатов инкремента
#и несколько раз вызываем для демонстрации
#есть смысл при реализации очередей или когда нужно много много больших
#значений
lst1 = (incr(i) for i in range(100))

def gen(lst1):
    for elem in lst1:
        yield elem
gen1 = gen(lst1)
print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))

'''print('Использовано памяти в конце:')
print(process.memory_info().rss)
print('Сколько занимает тип элемента списка:')
print(sys.getsizeof(type(lst[0])))
print('Использовано тип объекта процесса:')
print(sys.getsizeof(type(process)))'''
