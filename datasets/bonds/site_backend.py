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
    eng.print_p("Cредняя цена: " + str(metrics['mean_price']) + "%", file)
    eng.print_p("Cредняя доходность: " + str(metrics['mean_doh']) + "%", file)
    eng.print_p("Cредний объем торгов: " + str(metrics['mean_volume']) + " млрд. руб.", file)
    eng.div_close(file)
    eng.div_close(file)
    
#блок ссылок на архив ежедневных отчетов
def report_block(file, links, texts):
    eng.report_block(file)
    counter = 0
    eng.p_open(file)
    while counter < len(links):
        eng.href(file, links[counter], texts[counter])
        #eng.p_close(file)
        counter += 1
    eng.p_close(file)
    eng.div_close(file)
    eng.div_close(file)

#блок графиков общих данных
def dinamic_block(file):
    eng.dinamic_block(file)
    eng.print_p("Cредняя цена: " + " ", file)
    eng.print_img("site/price_dynamic.png", "Цена", file)
    eng.print_p("Cредняя доходность: " + " ", file)
    eng.print_img("site/doh_dynamic.png", "Цена", file)
    eng.print_p("Объем торгов: " + " ", file)
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
file = 'result/main.html'
report_dir = "result"
links = []
texts = []
#читаем из файла сырые данные
read(price, doh, volume, data)
count_metrics(price, doh, volume, metrics)
price_dynamics(data, price)
doh_dynamics(data, doh)
volume_dynamics(data, volume)
page_init(file)

arg = str(data[len(data) - 1])
common_block(file, arg, metrics)
gen_report_links()



report_block(file, links, texts)
dinamic_block(file)







