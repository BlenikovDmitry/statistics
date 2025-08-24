import matplotlib.pyplot as plt
import csv
import os
import pandas as pd
import html_engine as eng


'''
скрипт формирует папку papers, куда скидывает анализ всех бумаг за все время
и формирует общий список в файл papers.html
ВАЖНО! удали содержимое папки papers перед запуском, так как скрипт пересоздает все папки
чтобы добавить бумаги, которых раньше не было в списке
'''


'''
основной класс, содержит данные по бумагам
-наименование
-цена
-число сделок
-доходность последней сделки
-объем
-дата погашения
'''
class paper:
    def __init__(self, isin, price, count, doh, coupon, volume, enddate, dates):
        self.isin = isin
        self.price = price
        self.count = count
        self.doh = doh
        self.coupon = coupon
        self.volume = volume
        self.dates = dates
        self.enddate = enddate
    def update(self, price, count, doh, volume,dates):
        self.price = price
        self.count = count
        self.doh = doh
        self.volume = volume
        self.dates = dates
        


'''
функция создает объект бумаги и вносит в список если его еще нет
если он есть, то добавляет значения 
'''
def processing(paper_arr_names, paper_arr, raw_data, counter, date):
    isin = ''
    price = []
    count = []
    doh = []
    coupon = 0
    volume = []
    dates = []
    #dates = []
    enddate = '0'

    if raw_data.iloc[counter]['Наименование'] not in paper_arr_names:
        paper_arr_names.append(raw_data.iloc[counter]['Наименование'])
        isin = raw_data.iloc[counter]['Наименование']
        price.append(raw_data.iloc[counter]['Цена % средневзвешенная'])
        count.append(raw_data.iloc[counter]['Сделок шт.'])
        doh.append(raw_data.iloc[counter]['Дох посл сделки'])
        coupon = raw_data.iloc[counter]['Ставка купона']
        volume.append(raw_data.iloc[counter]['Объем в валюте'])
        enddate = raw_data.iloc[counter]['Дата погашения']
        dates.append(date)
        pap = paper(isin, price,count,doh,coupon,volume,enddate, dates)
        paper_arr.append(pap)
    else:
        price.clear()
        count.clear()
        doh.clear()
        coupon = 0
        volume.clear()
        dates.clear()
        enddate = '0'
        for item in paper_arr:
            if item.isin == raw_data.iloc[counter]['Наименование']:
                price = item.price.copy()
                count = item.count.copy()
                doh = item.doh.copy()
                volume = item.volume.copy()
                dates = item.dates.copy()
                price.append(raw_data.iloc[counter]['Цена % средневзвешенная'])
                count.append(raw_data.iloc[counter]['Сделок шт.'])
                doh.append(raw_data.iloc[counter]['Дох посл сделки'])
                volume.append(raw_data.iloc[counter]['Объем в валюте'])
                dates.append(date)
                item.update(price, count, doh, volume, dates)
                
#список бумаг(объектом класса paper)
paper_arr = []
#список имен бумаг(проще проверять наличие очередной бумаги в списке)
paper_arr_names = []
#сюда пишем dataframe очередного файла, чтобы 
raw_data = []
#переменная хранит путь к файлам
report_dir = 'result/site'
#получаем список файлов из папки
files = os.listdir(report_dir)

'''
бежим по списку файлов директории
открываем каждый файл, который содержит данные о результатах торгов, читаем его содержимое
и построчно прогоняем через функцию processing, которая запишет результаты в список paper_arr
'''
def collect(report_dir):
    #получаем список файлов из папки
    files = os.listdir(report_dir)
    counter = 0
    date = ''
    for file in files:
        if file[8:25] == 'ofz_cleared_short':
            date = file[0:8]
            raw_data = pd.read_csv(report_dir + '/' +file, encoding = 'Windows-1251')
            counter = 0
            while counter < len(raw_data['Наименование']):
                processing(paper_arr_names, paper_arr, raw_data, counter, date)
                counter += 1
'''
функция отрисовки графикоы цены, доходности и объема
'''
def graphic(markers, price,doh,volume, path):
    fig = plt.figure(figsize=(25,10))
    ax = fig.add_subplot()
    plt.xlabel("Дата")
    plt.ylabel("Цена")
    plt.xticks(rotation="vertical")
    ax.plot(markers, price, '-bo', linewidth=2, markersize=6, markerfacecolor='black')
    ax.grid()
    plt.savefig(path + 'price')
    plt.clf()
    plt.close()

    fig = plt.figure(figsize=(25,10))
    ax = fig.add_subplot()
    plt.xlabel("Дата")
    plt.ylabel("Доходность")
    plt.xticks(rotation="vertical")
    ax.plot(markers, doh, '-ro', linewidth=2, markersize=6, markerfacecolor='black')
    ax.grid()
    plt.savefig(path + 'doh')
    plt.clf()
    plt.close()

    fig = plt.figure(figsize=(25,10))
    ax = fig.add_subplot()
    plt.xlabel("Дата")
    plt.ylabel("Объем")
    plt.xticks(rotation="vertical")
    ax.plot(markers, volume, '-go', linewidth=2, markersize=6, markerfacecolor='black')
    ax.grid()
    plt.savefig(path + 'vol')
    

    plt.clf()
    plt.close()


'''
генератор индивидуальной страницы каждой бумаги
'''

def page_generator(file_fname, file_name, files_m):
    eng.init(file_fname)
    eng.init_main_uni(file_fname, file_name[0:len(file_name) - 1], file_name[0:len(file_name) - 1])
    eng.print_p("Цена: " + " ", file_fname)
    eng.print_img(file_name + files_m['price'], "Цена", file_fname)
    eng.print_p("Доходность: " + " ", file_fname)
    eng.print_img(file_name +files_m['doh'], "Цена", file_fname)
    eng.print_p("Объем торгов: " + " ", file_fname)
    eng.print_img(file_name + files_m['vol'], "Цена", file_fname)
    eng.div_close(file_fname)
    eng.div_close(file_fname)
    eng.close_document(file_fname)
'''
генератор общей страницы которая содержит список всех торгующихся офзшек
'''
def page_generator_all_papers(file_name, paper_arr):
    eng.init(file_name)
    eng.init_main_uni(file_name, 'Все выпуски офз', 'Все выпуски офз')
    eng.print_table_start(file_name)

    eng.print_tr_start(file_name)
    eng.print_td('Название', file_name)
    eng.print_td('Дата погашения', file_name)

    eng.print_tr_end(file_name)

    for item in paper_arr:
        eng.print_tr_start(file_name)
        eng.print_td("<a href="+"'papers/" +item.isin + ".html'>" + item.isin + '</a>', file_name)
        eng.print_td(item.enddate, file_name)
        eng.print_tr_end(file_name)

    
    eng.print_table_end(file_name)
    eng.div_close(file_name)
    eng.floor(file_name)
    eng.close_document(file_name)

    
    
'''
собираем данные по месяцам
важно, чтобы порядок соблюдался, так как данные пишутся в структуру данных как есть
чтобы не получилось так, чтобы апрель был перед январем
'''
#переменная хранит путь к файлам
report_dir = 'result/archive/jan/site'
collect(report_dir)

report_dir = 'result/archive/feb/site'
collect(report_dir)

report_dir = 'result/archive/mar/site'
collect(report_dir)
#к сожалению данные short стали собираться только с апреля 2025 года
report_dir = 'result/archive/apr/site'
collect(report_dir)


report_dir = 'result/archive/may/site'
collect(report_dir)


report_dir = 'result/archive/jun/site'
collect(report_dir)

report_dir = 'result/archive/jul/site'
collect(report_dir)

report_dir = 'result/site'
collect(report_dir)

'''
создаем папки при необходимости
и в каждую папку бросаем по 3 графика
после вызываем генератор индивидуальных страниц бумаги
ВНИМАНИЕ: общим перестроением лучше не увлекаться, так как общее перестроение занимает время
'''

for item in paper_arr:
    os.mkdir('result/papers/'+item.isin)

for item in paper_arr:
    graphic(item.dates, item.price,item.doh,item.volume, 'result/papers/'+item.isin[0:len(item.isin) - 1] + '/')

files_m = {'price': 'price.png', 'doh': 'doh.png', 'vol': 'vol.png'}
for item in paper_arr:
    page_generator('result/papers/'+item.isin + '.html',item.isin[0:len(item.isin) - 1] + '/', files_m)

page_generator_all_papers('result/papers.html', paper_arr)

print(len(paper_arr))
