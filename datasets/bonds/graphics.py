import matplotlib.pyplot as plt
import pandas as pd
import statistics
import html_engine as eng

#считываем сырые данные
ofz = pd.read_csv('result_ofz.csv', encoding = 'Windows-1251')


counter = 0
#прописываем пути для размещения графиков
path_jan = {'price': 'result/archive/jan/price_dynamic_jan.png', 'doh': 'result/archive/jan/doh_dynamic_jan.png', 'vol': 'result/archive/jan/volume_dynamic_jan.png'}
path_feb = {'price': 'result/archive/feb/price_dynamic_feb.png', 'doh': 'result/archive/feb/doh_dynamic_feb.png', 'vol': 'result/archive/feb/volume_dynamic_feb.png'}
path_mar = {'price': 'result/archive/mar/price_dynamic_mar.png', 'doh': 'result/archive/mar/doh_dynamic_mar.png', 'vol': 'result/archive/mar/volume_dynamic_mar.png'}
path_apr = {'price': 'result/archive/apr/price_dynamic_apr.png', 'doh': 'result/archive/apr/doh_dynamic_apr.png', 'vol': 'result/archive/apr/volume_dynamic_apr.png'}
path_may = {'price': 'result/archive/may/price_dynamic_may.png', 'doh': 'result/archive/may/doh_dynamic_may.png', 'vol': 'result/archive/may/volume_dynamic_may.png'}
path_jun = {'price': 'result/archive/jun/price_dynamic_jun.png', 'doh': 'result/archive/jun/doh_dynamic_jun.png', 'vol': 'result/archive/jun/volume_dynamic_jun.png'}
path_jul = {'price': 'result/archive/jul/price_dynamic_jul.png', 'doh': 'result/archive/jul/doh_dynamic_jul.png', 'vol': 'result/archive/jul/volume_dynamic_jul.png'}


#прописываем пути для размещения графиков
files_jan = {'price': 'price_dynamic_jan.png', 'doh': 'doh_dynamic_jan.png', 'vol': 'volume_dynamic_jan.png'}
files_feb = {'price': 'price_dynamic_feb.png', 'doh': 'doh_dynamic_feb.png', 'vol': 'volume_dynamic_feb.png'}
files_mar = {'price': 'price_dynamic_mar.png', 'doh': 'doh_dynamic_mar.png', 'vol': 'volume_dynamic_mar.png'}
files_apr = {'price': 'price_dynamic_apr.png', 'doh': 'doh_dynamic_apr.png', 'vol': 'volume_dynamic_apr.png'}
files_may = {'price': 'price_dynamic_may.png', 'doh': 'doh_dynamic_may.png', 'vol': 'volume_dynamic_may.png'}
files_jun = {'price': 'price_dynamic_jun.png', 'doh': 'doh_dynamic_jun.png', 'vol': 'volume_dynamic_jun.png'}
files_jul = {'price': 'price_dynamic_jul.png', 'doh': 'doh_dynamic_jul.png', 'vol': 'volume_dynamic_jul.png'}
#подсчет позиции откуда начинаются данные нужного месяца
#передаем ссылку на датасет и номер месяца, который интересует
def seek(ofz, month):
    counter = 0
    while counter < len(ofz):
        if ofz['Дата'][counter][4:5] == month:
            return counter
        counter += 1
#отрезаем кусочек данных интересующего месяца
#передаем датасет и номер месяца, который интересует
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
#отрисовка графиков цены, доходности и объема
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
#подсчет статистик за месяц для генерации страницы    
def stats(markers, price,doh, volume):
    price_med = statistics.median(price)
    doh_med = statistics.median(doh)
    volume_med = statistics.median(volume)
    return price_med, doh_med,volume_med

def page_generator(markers, price,doh, volume, file_name, price_med,doh_med,volume_med, header, files_m):
    eng.init(file_name)
    eng.init_main_uni(file_name, header)
    arg = " c " + markers[0] + " по " + markers[len(markers) - 1]
    eng.h2(file_name,arg)
    eng.print_p_main("Cредняя цена: " + str(round(price_med,2)) + "%", file_name)
    eng.print_p_main("Cредняя доходность: " + str(round(doh_med,2)) + "%", file_name)
    eng.print_p_main("Cредний объем торгов: " + str(volume_med) + " руб.", file_name)
    eng.div_close(file_name)
    eng.div_close(file_name)

    eng.dinamic_block(file_name)
    eng.print_p("Cредняя цена: " + " ", file_name)
    eng.href_download(file_name, files_m['price'], "Скачать")
    eng.print_img(files_m['price'], "Цена", file_name)
    eng.print_p("Cредняя доходность: " + " ", file_name)
    eng.href_download(file_name, files_m['doh'], "Скачать")
    eng.print_img(files_m['doh'], "Цена", file_name)
    eng.print_p("Объем торгов: " + " ", file_name)
    eng.href_download(file_name, files_m['vol'], "Скачать")
    eng.print_img(files_m['vol'], "Цена", file_name)
    eng.div_close(file_name)
    eng.div_close(file_name)
    eng.close_document(file_name)
    
    
    
    
        
#логика проста: отрезаем кусочек данных за интересующий месяц и вызываем отрисовку графика
markers, price,doh,volume = sliser(ofz, '1')
graphic(markers, price,doh,volume, path_jan)
price_med, doh_med,volume_med = stats(markers, price,doh,volume)

file_name = 'result/archive/jan/datajan.html'
header = 'Статистика за январь 2025'
page_generator(markers, price,doh,volume, file_name, price_med, doh_med,volume_med, header, files_jan)

'''print(round(price_med,2))
print(round(doh_med,2))
print(round(volume_med,2))'''

markers, price,doh,volume = sliser(ofz, '2')
graphic(markers, price,doh,volume, path_feb)
price_med, doh_med,volume_med = stats(markers, price,doh,volume)
file_name = 'result/archive/feb/datafeb.html'
header = 'Статистика за февраль 2025'
page_generator(markers, price,doh,volume, file_name, price_med, doh_med,volume_med, header, files_feb)

markers, price,doh,volume = sliser(ofz, '3')
graphic(markers, price,doh,volume, path_mar)
price_med, doh_med,volume_med = stats(markers, price,doh,volume)
file_name = 'result/archive/mar/datamar.html'
header = 'Статистика за март 2025'
page_generator(markers, price,doh,volume, file_name, price_med, doh_med,volume_med, header, files_mar)

markers, price,doh,volume = sliser(ofz, '4')
graphic(markers, price,doh,volume, path_apr)
price_med, doh_med,volume_med = stats(markers, price,doh,volume)
file_name = 'result/archive/apr/dataapr.html'
header = 'Статистика за апрель 2025'
page_generator(markers, price,doh,volume, file_name, price_med, doh_med,volume_med, header, files_apr)

markers, price,doh,volume = sliser(ofz, '5')
graphic(markers, price,doh,volume, path_may)
price_med, doh_med,volume_med = stats(markers, price,doh,volume)
file_name = 'result/archive/may/datamay.html'
header = 'Статистика за май 2025'
page_generator(markers, price,doh,volume, file_name, price_med, doh_med,volume_med, header, files_may)

markers, price,doh,volume = sliser(ofz, '6')
graphic(markers, price,doh,volume, path_jun)
price_med, doh_med,volume_med = stats(markers, price,doh,volume)
file_name = 'result/archive/jun/datajun.html'
header = 'Статистика за июнь 2025'
page_generator(markers, price,doh,volume, file_name, price_med, doh_med,volume_med, header, files_jun)

'''markers, price,doh,volume = sliser(ofz, '7')
graphic(markers, price,doh,volume, path_jul)'''



    


