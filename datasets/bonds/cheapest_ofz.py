import csv
import datetime
from datetime import datetime
from datetime import timedelta


"""
Скрипт выбора 4 выпусков с самой низкой ценой
1) выбираем самые дешевые облигации, загружая из ofz_cleared
2) считаем, сколько бумаг мы сможем купить на 10.000(можно поменять)
3) считаем сколько денег мы получим до даты погашения
4) выводим результат в cheapest_bonds_out.csv
"""
def read(name, kupon, end_data, price, last_doh):
    with open("ofz_cleared.csv", 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            name.append(str(row[1]))
            kupon.append(str(row[31]))
            end_data.append(str(row[17]))
            price.append(str(row[9]))
            last_doh.append(str(row[13]))
            nominal.append(str(row[7]))

"""
прописать также функции:
- максимальный купон - отбор
- оформить алгоритм подсчета и вывода в отдельныю функцию
- добавить конфиг, где будут настройки суммы, на которую будем покупать и количество таких бумаг
"""
def min_price(price):
    min_price = 10000
    index = 0
    counter = 1
    while counter < len(price):
        if(float(price[counter]) < float(min_price)):
            min_price = price[counter]
            index = counter
        counter +=1
    return index
    


name = []
kupon = []
end_data = []
price = []
last_doh = []
nominal = []

read(name, kupon, end_data, price, last_doh)

name_c = []
kupon_c = []
end_data_c = []
price_c = []
last_doh_c = []
count_bonds = []
summa_babla_year = []
summa_babla_all = []
nominal_c = []

#какую сумму можем позволить вложить и сколько отбираем бумаг
summa = 10000
sum_elems = 4

counter = 0
while counter < sum_elems:
    min_price_index = min_price(price)
    name_c.append(name[min_price_index])
    kupon_c.append(kupon[min_price_index])
    end_data_c.append(end_data[min_price_index])
    price_c.append(price[min_price_index])
    last_doh_c.append(last_doh[min_price_index])
    nominal_c.append(float(nominal[min_price_index]))
    name.pop(min_price_index)
    kupon.pop(min_price_index)
    end_data.pop(min_price_index)
    price.pop(min_price_index)
    last_doh.pop(min_price_index)
    counter +=1

counter = 0
while counter < sum_elems:
    count_bonds.append(int(summa / (float(price_c[counter]))))
    summa_babla_year.append(int(count_bonds[counter] * float(kupon_c[counter])))
    counter += 1

now = datetime.now()
counter = 0
for elems in end_data_c:
    time = datetime.strptime(str(end_data_c[counter]), '%d.%m.%y')
    delta = time - now
    tmp = int(delta.days / 365) * summa_babla_year[counter]
    summa_babla_all.append(tmp)
    counter += 1


code_out = ["код "]
kupon_out = ["купон(%) "]
end_data_out = ["дата погашения "]
price_out = ["цена "]
last_doh_out = ["дох посл сделки "]
nominal_out = ["номинал "]
summa_babla_year_out = ["сумма купонов за год"]
summa_babla_all_out = ["сумма купонов за весь срок"]
with open('cheapest_bonds_out.csv', 'w') as f:
    writer = csv.writer(f,  lineterminator='\n')
    writer.writerow(code_out + name_c)
    writer.writerow(kupon_out + kupon_c)
    writer.writerow(end_data_out + end_data_c)
    writer.writerow(price_out + price_c)
    writer.writerow(last_doh_out + last_doh_c)
    writer.writerow(nominal_out + nominal_c)
    writer.writerow(summa_babla_year_out + summa_babla_year)
    writer.writerow(summa_babla_all_out + summa_babla_all)

print(1)


