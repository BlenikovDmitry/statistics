import pandas as pd
import gc
import matplotlib.pyplot as plt

'''
добавить отдельно графики инфляции и кс
добавить на каждый границы стандартного отклонения

'''


'''
считали данные
почистили данные
сжали по используемой памяти
сделали срез
очистили память от лишних данных
'''
raw_set = pd.read_csv('cb.csv', encoding = 'Windows-1251', sep=';')


'''print('Использование памяти: ' + str(raw_set.memory_usage(index = False).sum()))'''

raw_set['Дата'] = raw_set['Дата'].astype('string')

raw_set['Ключевая ставка, % годовых'] = raw_set['Ключевая ставка, % годовых'].str.replace(',', '.')
raw_set['Инфляция, % г/г'] = raw_set['Инфляция, % г/г'].str.replace(',', '.')

raw_set['Ключевая ставка, % годовых'] = raw_set['Ключевая ставка, % годовых'].astype('float32')
raw_set['Инфляция, % г/г'] = raw_set['Инфляция, % г/г'].astype('float32')

raw_set['Ключевая ставка, % годовых'] = raw_set['Ключевая ставка, % годовых'].round(2)
raw_set['Инфляция, % г/г'] = raw_set['Инфляция, % г/г'].round(2)

final_set = raw_set.loc[:, ['Дата', 'Ключевая ставка, % годовых', 'Инфляция, % г/г']]

del raw_set
gc.collect()

'''
общий описательный анализ ключевой ставки и инфляции
c записью в файл desc.csv
попутно считаем корелляцию по Пирсону
c записью в файл correliation.csv

'''
correliation = final_set[['Ключевая ставка, % годовых', 'Инфляция, % г/г']].corr(method='pearson')
correliation.to_csv('correliation.csv', encoding = 'Windows-1251')
desc = final_set.describe(include = ['float32']).astype('float32').round(2)
desc.to_csv('desc.csv', encoding = 'Windows-1251')
del desc
del correliation
gc.collect()
'''
строим графики кс и инфляции, накладывая их друг на друга
генерируем результат в файл graphic.png
'''

fig, ax = plt.subplots(figsize=(25,10))
plt.title('Ключевая ставка / Инфляция')
plt.xlabel("месяц.год")
plt.ylabel("Ставка")

plt.xticks(rotation="vertical")
ax.plot(final_set['Дата'], final_set['Ключевая ставка, % годовых'], '-bo', linewidth=2, markersize=6, markerfacecolor='black')
ax.plot(final_set['Дата'], final_set['Инфляция, % г/г'], '-ro', linewidth=2, markersize=6, markerfacecolor='black')
plt.legend(['Ключевая ставка, % годовых', 'Инфляция, % г/г'])
ax.grid()
plt.savefig('graphic.png')



