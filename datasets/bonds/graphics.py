import matplotlib.pyplot as plt
import pandas as pd

#считываем сырые данные
ofz = pd.read_csv('result_ofz.csv', encoding = 'Windows-1251')

'''markers = []
price = []
doh = []
volume = []'''

counter = 0
path_jan = {'price': 'result/archive/jan/price_dynamic_jan.png', 'doh': 'result/archive/jan/doh_dynamic_jan.png', 'vol': 'result/archive/jan/volume_dynamic_jan.png'}
path_feb = {'price': 'result/archive/feb/price_dynamic_feb.png', 'doh': 'result/archive/feb/doh_dynamic_feb.png', 'vol': 'result/archive/feb/volume_dynamic_feb.png'}
path_mar = {'price': 'result/archive/mar/price_dynamic_mar.png', 'doh': 'result/archive/mar/doh_dynamic_mar.png', 'vol': 'result/archive/mar/volume_dynamic_mar.png'}
path_apr = {'price': 'result/archive/apr/price_dynamic_apr.png', 'doh': 'result/archive/apr/doh_dynamic_apr.png', 'vol': 'result/archive/apr/volume_dynamic_apr.png'}
path_may = {'price': 'result/archive/may/price_dynamic_may.png', 'doh': 'result/archive/may/doh_dynamic_may.png', 'vol': 'result/archive/may/volume_dynamic_may.png'}
path_jun = {'price': 'result/archive/jun/price_dynamic_jun.png', 'doh': 'result/archive/jun/doh_dynamic_jun.png', 'vol': 'result/archive/jun/volume_dynamic_jun.png'}
path_jul = {'price': 'result/archive/jul/price_dynamic_jul.png', 'doh': 'result/archive/jul/doh_dynamic_jul.png', 'vol': 'result/archive/jul/volume_dynamic_jul.png'}

def seek(ofz, month):
    counter = 0
    while counter < len(ofz):
        if ofz['Дата'][counter][4:5] == month:
            return counter
        counter += 1

def sliser(ofz, month):
    markers = []
    price = []
    doh = []
    volume = []
    counter = seek(ofz,month)
    
    while ofz['Дата'][counter][4:5] == month:
        markers.append(ofz['Дата'][counter])
        price.append(ofz['Средняя цена'][counter])
        doh.append(ofz['Средняя доходность последней сделки'][counter])
        volume.append(ofz['Объем торгов в рублях'][counter])

        counter += 1

    return markers, price,doh,volume

def graphic(markers, price,doh,volume, path):
    fig = plt.figure(figsize=(25,10))
    ax = fig.add_subplot()
    plt.xlabel("Дата")
    plt.ylabel("Цена")
    plt.xticks(rotation="vertical")
    ax.plot(markers, price, '-bo', linewidth=2, markersize=6, markerfacecolor='black')
    ax.grid()
    plt.savefig(path['price'])

    fig = plt.figure(figsize=(25,10))
    ax = fig.add_subplot()
    plt.xlabel("Дата")
    plt.ylabel("Доходность")
    plt.xticks(rotation="vertical")
    ax.plot(markers, doh, '-ro', linewidth=2, markersize=6, markerfacecolor='black')
    ax.grid()
    plt.savefig(path['doh'])

    fig = plt.figure(figsize=(25,10))
    ax = fig.add_subplot()
    plt.xlabel("Дата")
    plt.ylabel("Объем")
    plt.xticks(rotation="vertical")
    ax.plot(markers, volume, '-go', linewidth=2, markersize=6, markerfacecolor='black')
    ax.grid()
    plt.savefig(path['vol'])
    

        

markers, price,doh,volume = sliser(ofz, '1')
graphic(markers, price,doh,volume, path_jan)

markers, price,doh,volume = sliser(ofz, '2')
graphic(markers, price,doh,volume, path_feb)

markers, price,doh,volume = sliser(ofz, '3')
graphic(markers, price,doh,volume, path_mar)

markers, price,doh,volume = sliser(ofz, '4')
graphic(markers, price,doh,volume, path_apr)

markers, price,doh,volume = sliser(ofz, '5')
graphic(markers, price,doh,volume, path_may)

markers, price,doh,volume = sliser(ofz, '6')
graphic(markers, price,doh,volume, path_jun)

'''markers, price,doh,volume = sliser(ofz, '7')
graphic(markers, price,doh,volume, path_jul)'''



    


