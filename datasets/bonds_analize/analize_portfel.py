import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('russian_bonds.csv', delimiter = ';')


df['Цена покупки %'] = df['Цена покупки %'].astype(float)
df['Купон(руб.)'] = df['Купон(руб.)'].astype(float)
df['Кол-во'] = df['Кол-во'].astype(int)
df['Номинал'] = df['Номинал'].astype(int)
df['Число выплат в год'] = df['Число выплат в год'].astype(int)

price_mean = df['Цена покупки %'].mean()
coupon_mean = df['Купон(руб.)'].mean()
count_mean = df['Кол-во'].mean()
nominal_mean = df['Номинал'].mean()
count_coupon_mean = df['Число выплат в год'].mean()

df_central = pd.DataFrame(columns = ['Метрика','Цена покупки %', 'Купон(руб.)', 'Кол-во', 'Номинал', 'Число выплат в год'])

df_central.loc[len(df_central)] = ['Средние значения',
                   price_mean,
                   coupon_mean,
                   count_mean,
                   nominal_mean,
                   count_coupon_mean]

price_median = df['Цена покупки %'].median()
coupon_median = df['Купон(руб.)'].median()
count_median = df['Кол-во'].median()
nominal_median = df['Номинал'].median()
count_coupon_median = df['Число выплат в год'].median()

df_central.loc[len(df_central)] = ['Медиана',
                   price_median,
                   coupon_median,
                   count_median,
                   nominal_median,
                   count_coupon_median]


'''
Д - текущая доходность 1 бумаги - отдельным столбцом
Д = К / Ц * 100%, где:

К — сумма купонных выплат за период;
Ц — текущая рыночная цена облигации.
Подробнее на сайте Banki.ru https://www.banki.ru/news/daytheme/?id=10982360
в нашем случае:
К = coupon[counter_upper] * coupon_count[counter_upper](купон * число выплат в год)
Ц = bonds_price[counter_upper](цена бумаги на момент покупки с учетом рыночной цены в % поправленной на номинал покупки)
'''
df['Цена покупки с учетом номинала'] = df['Цена покупки %'] * df['Номинал'] / 100
df['Купонная доходность выпуска'] = (df['Купон(руб.)'] * df['Число выплат в год']) / df['Цена покупки с учетом номинала'] * 100
df['Купонная доходность выпуска'] = round(df['Купонная доходность выпуска'],2)
df['Купонный доход в год в рублях'] = (df['Кол-во'] * df['Номинал'] * (df['Купонная доходность выпуска'] / 100)).astype(int)


fig, ax = plt.subplots(figsize=(10,10))
plt.xticks(rotation="vertical")
ax.set_title("Распределение % купона по выпускам")
bars = ax.bar(df['Название'], df['Купонная доходность выпуска'], linewidth = 3.0, color = 'blue', ec='red')
ax.bar_label(bars)
ax.grid()
plt.savefig('result/coupon_distribution.png')

df.to_csv('result/analize.csv')
df_central.to_csv('result/metrics.csv')
result = df['Купонный доход в год в рублях'].sum() / (df['Кол-во'] * df['Номинал']).sum() * 100
result = round(result,2)
print(f'Купонная доходность всего портфеля: {result} % годовых')

