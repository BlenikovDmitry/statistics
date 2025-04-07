import pandas as pd

'''
примеры сводных таблиц
пример взят из сети и модицифирован под мои нужды
'''
data = {
   'Name': ['Alice', 'Bob', 'Charlie', 'Alice', 'Bob', 'Charlie', 'Alice'],
    'Month': ['January', 'January', 'January', 'February', 'February', 'February', 'January'],
    'Sales': [250, 300, 200, 400, 500, 300, 10000]
}
df = pd.DataFrame(data)
print(df)
#выводим сколько у кого в каком месяце суммарно продаж
pivot_table = df.pivot_table(values='Sales', index='Name', columns='Month', aggfunc='sum')
print(pivot_table)

#выводим сколько у кого в каком месяце средний чек
pivot_table = df.pivot_table(values='Sales', index='Name', columns='Month', aggfunc='mean')
print(pivot_table)

#те же действия, только с помощью groupby
#немного более коряво, но тоже работает для своих задач
print(df.groupby(['Name', 'Month']).sum())
print(df.groupby(['Name', 'Month']).mean())
