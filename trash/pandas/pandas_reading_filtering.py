import pandas as pd

#Читаем файл csv в кадр данных
ofz_set = pd.read_csv('ofz.csv', encoding = 'Windows-1251')

#выводим заголовок(первые 5 строк)
#print(ofz_set.head())
#выбираем из общего дата сета только столбцы ['Код','Наименование', 'Макс']
selected_data = ofz_set.loc[:,['Код','Наименование', 'Макс']]
print(selected_data)

#выбираем из общего дата сета все записи где максимальная цена > 90 и записываем в новый дата сет,
#ограничившись столбцами ['Код','Наименование', 'Макс']
selected_data = ofz_set[ofz_set['Макс'] > '90'].loc[:,['Код','Наименование', 'Макс']]
print(selected_data)

#убрали все строки, где валюта номинала доллар или евро
selected_data = ofz_set[ofz_set['Валюта номинала'] != 'USD'].loc[:,['Код','Наименование', 'Цена % средневзвешенная', 'Валюта номинала']]
selected_data = selected_data[selected_data['Валюта номинала'] != 'EUR']
print(selected_data)

#очистили от некорректных цен, преобразовали цены в float и выбрали те, что стоят больше номинала
selected_data = ofz_set
selected_data['Цена % средневзвешенная'] = selected_data['Цена % средневзвешенная'].str.replace('-', '0').str.replace(',','.').astype(float)

selected_data = selected_data[selected_data['Цена % средневзвешенная'] > 100].loc[:,['Код','Наименование', 'Цена % средневзвешенная', 'Валюта номинала']]
print(selected_data)


ofz_set['Цена % средневзвешенная'] = ofz_set['Цена % средневзвешенная'].astype(float)
selected_data = ofz_set[ofz_set['Цена % средневзвешенная'] > 100].loc[:,['Код','Наименование', 'Цена % средневзвешенная']]
print(selected_data)

#подсчитываем столбцы с пропущенными данными
selected_data = ofz_set
missing_values = selected_data.isnull().sum()

print(missing_values)

#приводим средневзвешенную цену к божескому виду
#подсчитываем столбцы с пропущенными данными
#заполняем столбец ставка купона каким то значением(3.14 в нашем случае)
#смотрим, что поменялось
#выводим всю выборку посмотреть
selected_data = ofz_set
#selected_data['Цена % средневзвешенная'] = selected_data['Цена % средневзвешенная'].str.replace('-', '0')
#selected_data['Цена % средневзвешенная'] = selected_data['Цена % средневзвешенная'].str.replace(',','.')
selected_data['Цена % средневзвешенная'] = selected_data['Цена % средневзвешенная'].astype(float)
selected_data = selected_data.loc[:,['Код','Наименование', 'Цена % средневзвешенная', 'Валюта номинала', 'Ставка купона', 'Эффективная доходность']]
missing_values = selected_data.isnull().sum()

print(missing_values)
selected_data['Ставка купона'] = selected_data['Ставка купона'].fillna(3.14)
missing_values = selected_data.isnull().sum()

print(missing_values)
print(selected_data)

#группировка значений и расчет статистик этих групп
#в примере группируем элементы по названию и узнаем число их повторений
#!!!Нужно больше примеров по группировке пригодится в будущем
selected_data = ofz_set
selected_data = selected_data.groupby('Наименование')['Ставка купона'].size().reset_index()
print(selected_data)

#фильтруем данные по непогашенному долгу
#для этого создаем фильтр в переменной mask и применяем к данным
selected_data = ofz_set
selected_data['Непогашенный долг'] = selected_data['Непогашенный долг'].str.replace('-', '0').str.replace(',','.').astype(float)
mask = selected_data['Непогашенный долг'] == 1000

filtered_data = selected_data[mask]
filtered_data = filtered_data.loc[:,['Код','Наименование', 'Непогашенный долг']]

print(filtered_data)

#фильтруем данные по непогашенному долгу сложным условием
#для этого создаем фильтр не подойдет, но можем фильтровать прямо здесь
#можно фиольтровать по нескольким столбцам
selected_data = ofz_set
#selected_data['Непогашенный долг'] = selected_data['Непогашенный долг'].str.replace('-', '0').str.replace(',','.').astype(float)
filtered_data = selected_data[(selected_data['Непогашенный долг'] > 1000) & (selected_data['Непогашенный долг'] < 10000)]

filtered_data = filtered_data.loc[:,['Код','Наименование', 'Непогашенный долг']]

print(filtered_data)

#попытка построить сводную таблицу.
#надо разбираться дальше
selected_data = ofz_set
#selected_data['Непогашенный долг'] = selected_data['Непогашенный долг'].str.replace('-', '0').str.replace(',','.').astype(float)
debt_pivot = selected_data.pivot_table(index = 'Код', columns = 'Наименование', values = 'Непогашенный долг', aggfunc = 'size')
print(debt_pivot)
#удаляем дубли из исходных данных
selected_data = ofz_set
selected_data.drop_duplicates(inplace=True)
print(selected_data)
