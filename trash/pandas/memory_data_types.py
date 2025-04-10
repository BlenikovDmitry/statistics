import numpy as np

'''
шпаргалка по типам данных
сколько памяти занимают и какие значения могут принимать
'''

#Целочисленные типы
int_types = ["int", "intc","intp", "int8", "int8", "int16","int32", "int64", "uint8", "uint16","uint32", "uint64"]
#вещественные типы
float_types = ["float", "float16", "float32", "float64"]

for elem in int_types:
    print(np.iinfo(elem))


for elem in float_types:
    print(np.finfo(elem))
    
