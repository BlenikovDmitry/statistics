import math
import statistics
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
import csv
import random
import tkinter as tk
from tkinter import ttk
import sys


"""

"""

x = []
y = []
#Чтение файла .csv
def read():
    with open("in.csv", 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            x.append(str(row[0]))
            y.append(float(row[1]))
#обработчики кнопок
"""
суть едина:
- очищаем canvas от того, что в нем было
- отрисовываем график в фигуре
- помещаем фигуру в canvas
- отрисовываем canvas
"""
def simple_graphic_button_click():
    for widget in frame1.winfo_children():
        widget.destroy()
    
    fig = plt.figure(figsize=(13,6))
    ax = fig.add_subplot(111)
    

    plt.xticks(rotation="vertical")
    plt.subplots_adjust(left=0.13, 
                    right=0.93, 
                    top=0.93, 
                    bottom= 0.22, 
                    wspace= 0.3, 
                    hspace=0.3)
    stde = statistics.stdev(y)
    average = statistics.mean(y)
    ax.plot(x,y, '-rh', linewidth=3, markersize=5, markerfacecolor='b')
    plt.axhline(average, color = 'green')
    plt.axhline(average + stde, color = 'black')
    plt.axhline(average - stde, color = 'black')
    plt.legend (('Факт','Среднее', 'Возможный коридор'))
    ax.grid()
    canvas = FigureCanvasTkAgg(fig, master=frame1)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    toolbar = NavigationToolbar2Tk(canvas,frame1)
    toolbar.update()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    plt.close()
    #sys.exit()
    
    
def scatterplot_button_click():
    for widget in frame1.winfo_children():
        widget.destroy()

    fig = plt.figure(figsize=(13,6), dpi=100)
    ax = fig.add_subplot(111)
    
    plt.xticks(rotation="vertical")
    plt.subplots_adjust(left=0.13, 
                    right=0.93, 
                    top=0.93, 
                    bottom= 0.22, 
                    wspace= 0.3, 
                    hspace=0.3)

    sizes = []
    colors = []
    counter = 0
    while counter < len(x):
        sizes.append(random.randint(20, 150))
        counter = counter + 1
    counter = 0
    while counter < len(x):
        colors.append(random.randint(20, 150))
        counter = counter + 1
    stde = statistics.stdev(y)
    average = statistics.mean(y)
    ax.scatter(x,y,s=sizes,c = colors)
    plt.axhline(average + stde, color = 'black')
    plt.axhline(average - stde, color = 'black')
    ax.grid()
    canvas = FigureCanvasTkAgg(fig, master=frame1)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    toolbar = NavigationToolbar2Tk(canvas,frame1)
    toolbar.update()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    plt.close()
    #sys.exit()

def histogram_button():
    for widget in frame1.winfo_children():
        widget.destroy()

    fig = plt.figure(figsize=(13,6), dpi=100)
    ax = fig.add_subplot(111)
    plt.xticks(rotation="vertical")
    plt.subplots_adjust(left=0.13, 
                    right=0.93, 
                    top=0.93, 
                    bottom= 0.22, 
                    wspace= 0.3, 
                    hspace=0.3)
    counter_iteration = 0
    distribution_average = []
    distribution_stde = []
    
    while counter_iteration < 10000:
        counter = 0
        markers_var = []
        data_var = []
        while counter < len(y):
                tmp = random.random() * len(y)
                data_var.append(y[int(tmp)])
                counter = counter + 1

        # среднее
        average = statistics.mean(data_var)
        distribution_average.append(average)
        
        counter_iteration = counter_iteration + 1

    ax.hist(distribution_average,50,linewidth = 1.5, color = "lightblue", ec="red")
    ax.grid()

    canvas = FigureCanvasTkAgg(fig, master=frame1)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    toolbar = NavigationToolbar2Tk(canvas,frame1)
    toolbar.update()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    plt.close()
    #sys.exit()

def histogram_stde_button_click():
    for widget in frame1.winfo_children():
        widget.destroy()
    
    fig = plt.figure(figsize=(13,6), dpi=100)
    ax = fig.add_subplot(111)

    plt.xticks(rotation="vertical")
    plt.subplots_adjust(left=0.13, 
                    right=0.93, 
                    top=0.93, 
                    bottom= 0.22, 
                    wspace= 0.3, 
                    hspace=0.3)
    counter_iteration = 0
    counter = 0
    tmp = 0
    distribution_stde = []
    while counter_iteration < 10000:
        counter = 0
        markers_var = []
        data_var = []
        while counter < len(y):
            tmp = random.random() * len(y)
            data_var.append(y[int(tmp)])
            counter = counter + 1
 
        stde = statistics.stdev(data_var)
       
        distribution_stde.append(stde)
    
        
        counter_iteration = counter_iteration + 1

    ax.hist(distribution_stde,50,linewidth = 1.5, color = "lightblue", ec="red")
    ax.grid()

    
    canvas = FigureCanvasTkAgg(fig, master=frame1)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    toolbar = NavigationToolbar2Tk(canvas,frame1)
    toolbar.update()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    plt.close()
    #sys.exit()

def barplot_button_click():
    for widget in frame1.winfo_children():
        widget.destroy()

    fig = plt.figure(figsize=(13,6), dpi=100)
    ax = fig.add_subplot(111)
    plt.xticks(rotation="vertical")
    plt.subplots_adjust(left=0.13, 
                    right=0.93, 
                    top=0.93, 
                    bottom= 0.22, 
                    wspace= 0.3, 
                    hspace=0.3)

    ax.bar(x,y,linewidth = 1.5, color = "lightblue", ec="red")
    ax.grid()
    canvas = FigureCanvasTkAgg(fig, master=frame1)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    toolbar = NavigationToolbar2Tk(canvas,frame1)
    toolbar.update()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    plt.close()
    #sys.exit()
    
    
    


#создаем окно
window = tk.Tk()
#задаем заголовок окну, размер и сразу задаем полноэкранный режим
window.title("рисовалка графиков")
#window.geometry("1200x1000")
window.state('zoomed')

#читаем файл данных
read()
#создаем фрейм для кнопок
frame = ttk.Frame(borderwidth="1", relief="solid", padding=["12", "10"])
#создаем фрейм для отрисовки графика
frame1 = ttk.Frame(borderwidth="1", relief="solid", padding=["12", "10"],height=10*100, width=12*100)
#создаем кнопки в фрейме frame
simple_graphic_button = tk.Button(frame,text = "Линейный график",width = "25", command = simple_graphic_button_click).grid(row="0", sticky="w")
scatterplot_button = tk.Button(frame,text = "Точечный график",width = "25", command = scatterplot_button_click).grid(row="1", sticky="w")
barplot_button = tk.Button(frame,text = "Столбцовый график",width = "25", command= barplot_button_click).grid(row="2", sticky="w")
histogram_average_button = tk.Button(frame,text = "Гистограмма среднего",width = "25", command = histogram_button).grid(row="3", sticky="w")
histogram_stde_button = tk.Button(frame,text = "Гистограмма отклонения",width = "25", command=histogram_stde_button_click).grid(row="4", sticky="w")
#картинка для привлечения внимания
image = tk.PhotoImage(file='warning.gif')
lbl = tk.Label(frame1, image=image).grid(row="0", sticky="n")
#размещаем оба фрейма на окне
frame.grid(row="0",column="0",sticky="nw")
frame1.grid(row="0",column="1", sticky="n")

window.mainloop()
