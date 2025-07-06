import matplotlib as plt
import pandas as pd

#считываем сырые данные
ofz = pd.read_csv('result_ofz.csv', encoding = 'Windows-1251')


price = []
doh = []
volume = []

counter = 0

while counter < len(ofz['Дата']):
    if ofz['Дата'][counter][4:5] == 1:
        
    counter += 1

    
    
