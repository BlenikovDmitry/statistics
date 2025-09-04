import statistics
import matplotlib.pyplot as plt
import random

"""

Бутстрапируем полученную выборку, отрисовываем распределение среднего и
стандартного отклонения(count_iterations итераций)
генерируем графики

"""
        
        

def bootstrap(data, count_iterations):
    counter_iteration = 0
    counter = 0
    distribution_average = []
    distribution_median = []
    distribution_stde = []
    average = statistics.mean(data)
    stde = statistics.stdev(data)
    while counter_iteration < count_iterations:
        counter = 0
        data_var = []
        while counter < len(data):
            data_var.append(data[int(random.random() * len(data))])
            counter = counter + 1
       
        distribution_average.append(statistics.mean(data_var))
        distribution_stde.append(statistics.stdev(data_var))
    
        
        counter_iteration += 1
     

    return distribution_average, distribution_stde, average, stde
