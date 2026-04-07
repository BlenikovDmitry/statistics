import statistics
import matplotlib.pyplot as plt
import random

"""

Бутстрапируем полученную выборку, отрисовываем распределение среднего (count_iterations итераций)
генерируем графики

"""
        
        

def bootstrap(data, count_iterations, flag):
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
    if flag == 'ks':
        fig = plt.figure(figsize=(6,6))
        ax = fig.add_subplot()
        ax.set_title("Распределение среднего")
        ax.hist(distribution_average, 50, color = "blue", ec="lightblue", edgecolor="black", rwidth = 5)
        plt.axvline(average,linewidth=4, color='g', label = "Среднее изначальное")
        plt.xlabel("Ставка(%)")
        plt.ylabel("Количество")
        plt.legend()
        ax.grid()

    if flag == 'infl':
        fig = plt.figure(figsize=(6,6))
        ax = fig.add_subplot()
        ax.set_title("Распределение среднего")
        ax.hist(distribution_average, 50, color = "red", ec="lightblue", edgecolor="black", rwidth = 5)
        plt.axvline(average,linewidth=4, color='g', label = "Среднее изначальное")
        plt.xlabel("Инфляция(%)")
        plt.ylabel("Количество")
        plt.legend()
        ax.grid()
    

    return plt
