import pandas as pd
import matplotlib.pyplot as plt
import generator_ofz as gen


'''
движок очистки данных и генерации отчета по дню
будет заменой работающему движку ofz.ipnb

Чтобы работало, нужно перенести функционал:
- протестировать и сопоставить с результатом работы действующего движка

'''

'''
считывание и обработка сырых данных, приведение к нужному вижу
результат:
- файл ofz_cleared.csv - очищенные но не обработанные данные
- файл ofz_cleared_short.csv - очищенные и обработанные данные(сокращенный формат)
- файл statistics.csv - статистики 
'''
MAX_DEV = 4

#считываем сырые данные
ofz = pd.read_csv('ofz.csv', encoding = 'Windows-1251')

#столбцы, которые будем преобразовывать и вычищать от всякого
cols_to_float = ['Непогашенный долг','Сумма купона','Сделок шт.','Объем в валюте','Цена % средневзвешенная',
        'Мин','Макс','Цена посл %', 'Дох посл сделки','Доходность к оферте',  'Доходность посл. Купона', 'Закрытия %'
        , 'Дюрация дней', 'Вмененная RUONIA',	'Вмененная инфляция', 'BEI']
#из нужных столбцов убираем знаки '-', ',' и преобразуем в тип float
for i in cols_to_float:
   ofz[i] = ofz[i].str.replace('-', '0')
   ofz[i] = ofz[i].str.replace(',', '.')
   ofz[i] = ofz[i].astype(float)
   
#считаем в каждом столбце пустые строки и заполняем их
#всякое непонятное заменяем на 0
missing_values = ofz.isnull().sum()

ofz['Дата оферты'] = ofz['Дата оферты'].fillna('0')
ofz['Дата посл сделки'] = ofz['Дата посл сделки'].fillna('0')

ofz['Эффективная доходность'] = ofz['Эффективная доходность'].fillna('0')

ofz['Маркер КБД'] = ofz['Маркер КБД'].fillna('0')

ofz['Дюрация срвзвеш'] = ofz['Дюрация срвзвеш'].fillna('0')
ofz['Z spread'] = ofz['Z spread'].fillna('0')
ofz['G spread'] = ofz['G spread'].fillna('0')
#в дату расчета доходности подставляем дату последней сделки
#так как предполагаем, что доходность меняется со сделкими, а их на текущую дату может и не быть
ofz['Дата расчета дох'] = ofz['Дата расчета дох'].fillna(ofz['Дата посл сделки'])
#ставка купона = сумма купона * 2(тк выплат 2 раза в год) и переводим в проценты
ofz['Ставка купона'] = ofz['Ставка купона'].fillna(round((ofz['Сумма купона'] * 2) / ofz['Непогашенный долг'] * 100, 2))

#убеждаемся, что все заполнено
missing_values = ofz.isnull().sum()
print(missing_values)

file_name = ofz['Дата посл сделки'].values[:1].astype(str)
file_name = str(file_name)
file_name = file_name[2:10]

#выводим в файл все данные очищенные
ofz.to_csv('result/site/' + file_name +'ofz_cleared.csv', encoding = 'Windows-1251')

#фильтруем данные по доходности последней сделки  и выводим в отдельный файл
#доходность последней сделки должна быть больше нуля
selected_data = ofz[ofz['Дох посл сделки'] > 0].loc[:,['Наименование','Цена % средневзвешенная','Сделок шт.', 'Дох посл сделки','Ставка купона','Объем в валюте', 'Дата погашения']]
#выводим данные в файл
selected_data.to_csv('result/site/' + file_name+'ofz_cleared_short.csv', encoding = 'Windows-1251')

print(selected_data)
print(ofz)
#подсчет статистик по очищенным данным
#создаем кадр данных и подсчитываем статистики
#результат записываем в файл result_ofz.csv предварительно очистив от дублей

statistics = pd.DataFrame(columns=['Дата','Средняя ставка купона', 'Отклонение средней ставки купона','Средняя доходность последней сделки', 'Отклонение доходности последней сделки'
                                   ,'Средняя цена', 'Отклонение средней цены', 'Объем торгов в рублях'])

statistics = pd.read_csv('result_ofz.csv', encoding = 'Windows-1251')
#print(statistics)
statistics.loc[file_name] = [file_name, round(selected_data['Ставка купона'].mean(), 2),round(selected_data['Ставка купона'].std(), 2),
                       round(selected_data['Дох посл сделки'].mean(),2), round(selected_data['Дох посл сделки'].std(),2),round(selected_data['Цена % средневзвешенная'].mean(),2),
                       round(selected_data['Цена % средневзвешенная'].std(), 2),round(selected_data['Объем в валюте'].sum(),2)]

statistics.drop_duplicates(inplace = True)
duplicates = statistics.duplicated().sum()
#print(duplicates)


#выводим в файл статистики
statistics.to_csv('result_ofz.csv', encoding = 'Windows-1251', index = False)

'''
генерация графиков
данные уже хранятся в структуре selected_data
'''

#купонная доходность несортированный
fig, ax = plt.subplots(figsize=(25,10))
plt.title("Купонная доходность")
plt.xlabel("Выпуск")
plt.ylabel("Купон")

plt.xticks(rotation="vertical")
ax.plot(selected_data['Наименование'],selected_data['Ставка купона'], '-rh', linewidth=3, markersize=5, markerfacecolor='b')
ax.grid(which = 'both')
plt.savefig('result/site/' + file_name + 'kupon_ofz.png')
#дох посл сделки несортированная
fig, ax = plt.subplots(figsize=(25,10))
ax.set_title("Доходность общая по последней сделке")
plt.xlabel("Выпуск")
plt.ylabel("Доходность последней сделки")
plt.xticks(rotation="vertical")
ax.plot(selected_data['Наименование'],selected_data['Дох посл сделки'], '-gh', linewidth=3, markersize=5, markerfacecolor='b')
ax.grid(which = 'both')
plt.savefig('result/site/' + file_name + 'dohod_eff_ofz.png')
#цена несортированная
fig, ax = plt.subplots(figsize=(25,10))
ax.set_title("Цена")
plt.xlabel("Выпуск")
plt.ylabel("Цена")
plt.xticks(rotation="vertical")
ax.plot(selected_data['Наименование'],selected_data['Цена % средневзвешенная'], '-bh', linewidth=3, markersize=5, markerfacecolor='b')
ax.grid(which = 'both')
plt.savefig('result/site/' + file_name + 'price_ofz.png')


#отрисовываем распределение купонов
fig, ax = plt.subplots(figsize=(25,10))
plt.xticks(rotation="vertical")
ax.set_title("Распределение % купона по выпускам")
ax.bar(selected_data['Наименование'], selected_data['Ставка купона'], linewidth = 3.0, color = 'blue', ec='red')
ax.grid(which = 'both')
plt.savefig('result/site/' + file_name + 'interest_distribution_ofz.png')
#цена сортированная
selected_data = selected_data.sort_values(by='Цена % средневзвешенная', ascending=False)
fig, ax = plt.subplots(figsize=(25,10))
ax.set_title("Цена")
plt.xlabel("Выпуск")
plt.ylabel("Цена")
plt.xticks(rotation="vertical")
ax.plot(selected_data['Наименование'],selected_data['Цена % средневзвешенная'], '-bh', linewidth=3, markersize=5, markerfacecolor='b')
ax.grid(which = 'both')
plt.savefig('result/site/' + file_name + 'price_ofz_sorted.png')
#купонная доходность сортированная
selected_data = selected_data.sort_values(by='Ставка купона', ascending=False)
fig, ax = plt.subplots(figsize=(25,10))
plt.title("Купонная доходность")
plt.xlabel("Выпуск")
plt.ylabel("Купон")

plt.xticks(rotation="vertical")
ax.plot(selected_data['Наименование'],selected_data['Ставка купона'], '-rh', linewidth=3, markersize=5, markerfacecolor='b')
ax.grid(which = 'both')
plt.savefig('result/site/' + file_name + 'kupon_ofz_sorted.png')
#график погашения сортированный
selected_data['Дата погашения'] = pd.to_datetime(selected_data['Дата погашения'], format='mixed')
selected_data = selected_data.sort_values(by='Дата погашения', ascending=False)
fig, ax = plt.subplots(figsize=(25,10))
plt.xticks(rotation="vertical")
ax.set_title("График погашения")
ax.plot(selected_data['Наименование'],selected_data['Дата погашения'], '-bh', linewidth=3, markersize=5, markerfacecolor='b')
ax.grid(which = 'both')
plt.savefig('result/site/' + file_name + 'end_graphic_ofz.png')

#дох посл сделки сортированная
selected_data = selected_data.sort_values(by='Дох посл сделки', ascending=False)
fig, ax = plt.subplots(figsize=(25,10))
ax.set_title("Доходность общая по последней сделке")
plt.xlabel("Выпуск")
plt.ylabel("Доходность последней сделки")
plt.xticks(rotation="vertical")
ax.plot(selected_data['Наименование'],selected_data['Дох посл сделки'], '-gh', linewidth=3, markersize=5, markerfacecolor='b')
ax.grid(which = 'both')
plt.savefig('result/site/' + file_name + 'dohod_eff_ofz_sorted.png')

#объем торгов
selected_data['Объем в валюте'] = selected_data['Объем в валюте'].astype(float)
selected_data = selected_data.sort_values(by='Объем в валюте', ascending=False)
fig = plt.figure(figsize=(25,10))
ax = fig.add_subplot(1,1,1)
plt.xticks(rotation="vertical")
ax.set_title("Объем торгов")
ax.bar(selected_data['Наименование'], selected_data['Объем в валюте'], width=1, color = "lightblue", edgecolor="red", linewidth=0.7)
ax.grid(which = 'both')
plt.savefig('result/site/' + file_name + 'volume_ofz_sorted.png')

'''
генерация страницы отчета
'''
file_out = 'result/' + file_name + '.html'
gen.init(file_name, file_out)

gen.statistic_header(file_out)

rows = [str(round(selected_data['Ставка купона'].mean(), 2)) + '%',str(round(selected_data['Ставка купона'].std(), 2)) + '%',
                       str(round(selected_data['Дох посл сделки'].mean(),2)) + '%', str(round(selected_data['Дох посл сделки'].std(),2)) + '%',
                       str(round(selected_data['Цена % средневзвешенная'].mean(),2)) + '%',
                       str(round(selected_data['Цена % средневзвешенная'].std(), 2)) + '%',round(selected_data['Объем в валюте'].sum(),2)]
gen.statistic_body(rows, file_out)
gen.graphics(file_out, file_name)


