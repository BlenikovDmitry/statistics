
import csv
import os
import pandas as pd


price = []
count = []
doh = []


paper = []


class paper:
    def __init__(self, isin, price, count, doh, coupon, volume, enddate):
        self.isin = isin
        self.price = price
        self.count = count
        self.doh = doh
        self.coupon = coupon
        self.volume = volume
        self.enddate = enddate
    def update(self, price, count, doh, volume):
        self.price = price
        self.count = count
        self.doh = doh
        self.volume = volume
        



def processing(paper_arr_names, paper_arr, raw_data, counter):
    isin = ''
    price = []
    count = []
    doh = []
    coupon = 0
    volume = []
    enddate = '0'

    if raw_data.iloc[counter]['Наименование'] not in paper_arr_names:
        #print(raw_data.iloc[counter]['Наименование'])
        paper_arr_names.append(raw_data.iloc[counter]['Наименование'])
        isin = raw_data.iloc[counter]['Наименование']
        price.append(raw_data.iloc[counter]['Цена % средневзвешенная'])
        count.append(raw_data.iloc[counter]['Сделок шт.'])
        doh.append(raw_data.iloc[counter]['Дох посл сделки'])
        coupon = raw_data.iloc[counter]['Ставка купона']
        volume.append(raw_data.iloc[counter]['Объем в валюте'])
        enddate = raw_data.iloc[counter]['Дата погашения']
        pap = paper(isin, price,count,doh,coupon,volume,enddate)
        paper_arr.append(pap)
    else:
        #print(raw_data.iloc[counter]['Наименование'])
        price.clear()
        count.clear()
        doh.clear()
        coupon = 0
        volume.clear()
        enddate = '0'
        for item in paper_arr:
            #print(str(item.isin))
            if item.isin == raw_data.iloc[counter]['Наименование']:
                price = item.price.copy()
                count = item.count.copy()
                doh = item.doh.copy()
                volume = item.volume.copy()
                price.append(raw_data.iloc[counter]['Цена % средневзвешенная'])
                count.append(raw_data.iloc[counter]['Сделок шт.'])
                doh.append(raw_data.iloc[counter]['Дох посл сделки'])
                volume.append(raw_data.iloc[counter]['Объем в валюте'])
                item.update(price, count, doh, volume)
                



#pap = paper(isin, price,count,doh,coupon,volume,enddate)
paper_arr = []
paper_arr_names = []
raw_data = []
report_dir = 'result/site'
files = os.listdir(report_dir)
print(files[7][8:25])

counter = 0
for file in files:
    if file[8:25] == 'ofz_cleared_short':
        raw_data = pd.read_csv('result/site/' +file, encoding = 'Windows-1251')
        counter = 0
        while counter < len(raw_data['Наименование']):
            processing(paper_arr_names, paper_arr, raw_data, counter)
           
            counter += 1

'''for elem in paper_arr:
    print(elem.isin)
    print(elem.doh)'''

