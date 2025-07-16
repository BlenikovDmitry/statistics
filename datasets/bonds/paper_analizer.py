
import csv
import os
import pandas as pd


price = []
count = []
doh = []


paper = []

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


#переменная хранит путь к файлам
report_dir = 'result/site'
collect(report_dir)

'''report_dir = 'result/archive/jan/site'
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
collect(report_dir)'''

for elem in paper_arr:
    print(elem.isin)
    print(elem.doh)
    print(elem.dates)

print(len(paper_arr))
