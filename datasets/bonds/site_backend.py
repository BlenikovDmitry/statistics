import csv
import statistics
import matplotlib.pyplot as plt


#читаем исходный файл 
def read(price, doh, volume, data):
    with open("result_ofz.csv", 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            price.append(float(row[5]))
            doh.append(float(row[3]))
            volume.append(float(row[7]))
            data.append(str(row[0]))
            
        price.pop(0)
        volume.pop(0)
        doh.pop(0)
        data.pop(0)
            
            
#считаем средние метрики           
def count_metrics(price, doh, volume, metrics):
    metrics["mean_price"] = round(statistics.mean(price), 2)
    metrics["mean_doh"] = round(statistics.mean(doh), 2)
    mean_volume = statistics.mean(volume)
    #средний объем переводим в строку, чтобы отрезать первые три символа
    #для сокращения
    mean_volume = str(mean_volume)
    metrics["mean_volume"] = mean_volume[0:3]
    print(metrics)

def price_dynamics(data, price):
    fig = plt.figure(figsize=(25,10))
    ax = fig.add_subplot()
    plt.xlabel("Дата")
    plt.ylabel("Цена")
    plt.xticks(rotation="vertical")
    ax.plot(data, price, '-bo', linewidth=2, markersize=6, markerfacecolor='black')
    ax.grid()
    plt.savefig('result/site/price_dynamic.png')

def doh_dynamics(data, doh):
    fig = plt.figure(figsize=(25,10))
    ax = fig.add_subplot()
    plt.xlabel("Дата")
    plt.ylabel("Доходность")
    plt.xticks(rotation="vertical")
    ax.plot(data, doh, '-ro', linewidth=2, markersize=6, markerfacecolor='black')
    ax.grid()
    plt.savefig('result/site/doh_dynamic.png')

def volume_dynamics(data, volume):
    fig = plt.figure(figsize=(25,10))
    ax = fig.add_subplot()
    plt.xlabel("Дата")
    plt.ylabel("Объем")
    plt.xticks(rotation="vertical")
    ax.plot(data, volume, '-go', linewidth=2, markersize=6, markerfacecolor='black')
    ax.grid()
    plt.savefig('result/site/volume_dynamic.png')

    

data = []
price = []
doh = []
volume = []
metrics = {}
#читаем из файла сырые данные
read(price, doh, volume, data)
count_metrics(price, doh, volume, metrics)
price_dynamics(data, price)
doh_dynamics(data, doh)
volume_dynamics(data, volume)



