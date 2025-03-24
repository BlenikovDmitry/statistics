import pandas as pd

ofz = pd.read_csv('ofz_cleared_all.csv', encoding = 'Windows-1251')

#выборка нужных столбцов в новый кадр
selected_data = ofz[['Наименование', 'Ставка купона', 'Объем в валюте']]
print(selected_data)
#число дубликатов строк
duplicates = ofz.duplicated().sum()
print(duplicates)
#убрали дубликаты в исходном дата сете и подсчитали пропущенные данные
ofz.drop_duplicates(inplace = True)
missing = ofz.isnull().sum()
print(missing)
print(ofz)

#примеры группировки
#Группируем по наименованию и подсчитываем среднюю ставку купона по выпускам
#Группируем по непогашенному долгу и считаем количество вариантов номиналов
group_name = ofz.groupby('Наименование')['Ставка купона'].mean().reset_index()
print(group_name)
group_name = ofz.groupby('Непогашенный долг').size().reset_index()
print(group_name)
#пишем маску для выборки всех бумаг, где номинал 1000 рублей
mask = ofz['Непогашенный долг'] == 1000
selected_data = ofz[mask]
print(selected_data)
#выбираем бумаги с непогашенным долгом  == 1000 рублей и суммой купона более 20 рублей
#группируем по сумме купона
selected_data = ofz[(ofz['Непогашенный долг'] == 1000) & (ofz['Сумма купона'] > 20)]
group_name = selected_data.groupby('Наименование')['Сумма купона'].sum().reset_index()
print(selected_data)
print(group_name)

#выбираем бумаги с непогашенным долгом  не равным 1000 рублей и суммой купона менее или равно 20 рублей
#группируем по сумме купона
selected_data = ofz[~(ofz['Непогашенный долг'] == 1000) & ~(ofz['Сумма купона'] > 20)]
group_name = selected_data.groupby('Наименование')['Сумма купона'].sum().reset_index()
print(selected_data)
print(group_name)

#выбираем бумаги с непогашенным долгом равным 1000 рублей или суммой купона более 20 рублей
#группируем по сумме купона
selected_data = ofz[(ofz['Непогашенный долг'] == 1000) | (ofz['Сумма купона'] > 20)]
group_name = selected_data.groupby('Наименование')['Сумма купона'].sum().reset_index()
print(selected_data)
print(group_name)
#выбираем бумаги, где в наименовании содержится 26238 или 26245                 
selected_data = ofz[(ofz['Наименование'].str.contains('26238') | ofz['Наименование'].str.contains('26245'))]
print(selected_data)
#выбираем все бумаги, у которых осталось менее 5 лет до погашения
#можно фильтром, но здесь сделал запросом

#меняем тип данных столбца Дата погашения на тип даты
ofz['Дата погашения'] = pd.to_datetime(ofz['Дата погашения'])
#получаем сегодняшнюю дату
now = pd.to_datetime('today').date()
#прибавляем 5 лет
end = now + pd.DateOffset(years= 5)
end = end.date()
#делаем выборку всех бумаг, у которых дата погашения < 5 лет
selected_data = ofz.query('`Дата погашения` <= @end')
#попутно группируем в удобный формат
group_name = selected_data.groupby('Наименование')['Сумма купона'].sum().reset_index()
print(group_name)
#все то же самое, только еще берем бумаги до 5 лет и сумма купона < 50 рублей
selected_data = ofz.query('`Дата погашения` <= @end and `Сумма купона` < 50')
group_name = selected_data.groupby('Наименование')['Сумма купона'].sum().reset_index()
print(group_name)

