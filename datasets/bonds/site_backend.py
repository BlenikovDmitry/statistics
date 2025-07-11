import csv
import statistics
import matplotlib.pyplot as plt
import html_engine as eng
import os


#читаем исходный файл 
def read(price, doh, volume, data):
    with open("result_ofz.csv", 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            price.append(row[5])
            doh.append(row[3])
            volume.append(row[7])
            data.append(row[0])
            
        price.pop(0)
        volume.pop(0)
        doh.pop(0)
        data.pop(0)

        counter = 0
        while counter < len(price):
            price[counter] = float(price[counter])
            doh[counter] = float(doh[counter])
            volume[counter] = float(volume[counter])
            counter += 1
    #ограничиваем отрисовку графиков и подсчет статистик последними 100 значениями(чтобы график не расползался на главной)        
    delimiter = len(price) - 100
    counter = 0
    while counter < delimiter:
        price.pop(0)
        volume.pop(0)
        doh.pop(0)
        data.pop(0)
        
        counter += 1

            
            
#считаем метрики
# так как бралось среднее от среднего, принял решение брать не среднее значение
# в метрику, а последнее
def count_metrics(price, doh, volume, metrics):
    metrics["price"] = round(price[len(price) - 1], 2)
    metrics["doh"] = round(doh[len(doh) - 1], 2)
    last_volume = round(volume[len(volume) - 1], 0)

    last_volume = str(last_volume)
    metrics["volume"] = last_volume

#генерация графика динамики цены
def price_dynamics(data, price):
    fig = plt.figure(figsize=(25,10))
    ax = fig.add_subplot()
    plt.xlabel("Дата")
    plt.ylabel("Цена")
    plt.xticks(rotation="vertical")
    ax.plot(data, price, '-bo', linewidth=2, markersize=6, markerfacecolor='black')
    ax.grid()
    plt.savefig('result/site/price_dynamic.png')
#генерация графика динамики доходности
def doh_dynamics(data, doh):
    fig = plt.figure(figsize=(25,10))
    ax = fig.add_subplot()
    plt.xlabel("Дата")
    plt.ylabel("Доходность")
    plt.xticks(rotation="vertical")
    ax.plot(data, doh, '-ro', linewidth=2, markersize=6, markerfacecolor='black')
    ax.grid()
    plt.savefig('result/site/doh_dynamic.png')
#генерация графика динамики объема
def volume_dynamics(data, volume):
    fig = plt.figure(figsize=(25,10))
    ax = fig.add_subplot()
    plt.xlabel("Дата")
    plt.ylabel("Объем")
    plt.xticks(rotation="vertical")
    ax.plot(data, volume, '-go', linewidth=2, markersize=6, markerfacecolor='black')
    ax.grid()
    plt.savefig('result/site/volume_dynamic.png')


'''
генерация главной страницы сайта
'''
#создание файла и запись заголовка
def page_init(file):
    eng.init(file)
    eng.init_main(file)
#блок общих данных статистики
def common_block(file, arg, metrics):
    eng.h2(file, arg)
    eng.print_p_main("Cредняя цена: " + str(metrics['price']) + "%", file)
    eng.print_p_main("Cредняя доходность: " + str(metrics['doh']) + "%", file)
    eng.print_p_main("Cредний объем торгов: " + str(metrics['volume']) + " руб.", file)
    eng.div_close(file)
    eng.div_close(file)
    
#блок ссылок на архив ежедневных отчетов
def report_block(file, links, texts):
    eng.report_block(file)
    counter = 0
    eng.p_open(file)
    while counter < len(links):
        eng.href(file, links[counter], texts[counter])
        counter += 1
    eng.p_close(file)
    eng.div_close(file)
    eng.div_close(file)

#блок графиков общих данных
def dinamic_block(file):
    eng.dinamic_block(file)
    eng.print_p("Cредняя цена: " + " ", file)
    eng.href_download(file, "site/price_dynamic.png", "Скачать")
    eng.print_img("site/price_dynamic.png", "Цена", file)
    eng.print_p("Cредняя доходность: " + " ", file)
    eng.href_download(file, "site/doh_dynamic.png", "Скачать")
    eng.print_img("site/doh_dynamic.png", "Цена", file)
    eng.print_p("Объем торгов: " + " ", file)
    eng.href_download(file, "site/volume_dynamic.png", "Скачать")
    eng.print_img("site/volume_dynamic.png", "Цена", file)
    eng.div_close(file)
    eng.div_close(file)
    eng.close_document(file)
#получаем список файлов директории для генерации ссылок на отчеты
def get_reports():
    # Получаем список файлов
    files = os.listdir(report_dir)
    # Выводим список файлов
    return files
#генерация блока, содержащего ежедневные отчеты   
def gen_report_links():
    files = get_reports()
    for elem in files:
        if elem[9:13] == 'html':
            links.append(elem)
            link_text = elem[0:8]
            texts.append(link_text)
    links.append('archive.html')
    texts.append('Архив')
    
    

data = []
price = []
doh = []
volume = []
metrics = {}
file = 'result/index.html'
report_dir = "result"
links = []
texts = []
#читаем из файла сырые данные
read(price, doh, volume, data)
#подсчитываем метрики для вывода в блок общих данных
count_metrics(price, doh, volume, metrics)
#генерация графика динамики цены
price_dynamics(data, price)
#генерация графика динамики доходности
doh_dynamics(data, doh)
#генерация графика динамики объема торгов
volume_dynamics(data, volume)
'''
генерация главной страницы
'''
page_init(file)
date_start = str(data[0])
date_end = str(data[len(data) - 1])
arg = " c " + date_start + " по " + date_end
common_block(file, arg, metrics)
gen_report_links()



report_block(file, links, texts)
dinamic_block(file)
'''
///////////////////////////////
'''







