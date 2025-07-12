import csv
import os


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


isin = 'ru12345'
price = [100,98,90]
count = [12,13,14]
doh = [10,11,12]
coupon = 15
volume = [1234567,123,45678]
enddate = '12.03.2026'

pap = paper(isin, price,count,doh,coupon,volume,enddate)

'''print(pap.isin)
print(pap.price[2])
print(pap.count)
print(pap.doh)
print(pap.coupon)
print(pap.volume[0])
print(pap.enddate)'''
report_dir = 'result/site'
files = os.listdir(report_dir)
print(files[7][8:25])

for file in files:
    if file[8:25] == 'ofz_cleared_short':
        #здесь пишем метод чтения и добавления/обновления данных в объект
