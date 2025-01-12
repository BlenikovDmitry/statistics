import matplotlib.pyplot as plt
import csv


markers = ['2010', '2011', '2012', '2013','2014','2015','2016','2017','2018',
           '2019','2020','2021','2022','2023','2024']
data = [2579.128, 4003.322, 4645.255, 5338.126, 5759.200, 7160.043, 7602.353
        ,9137.261, 9137.513, 10739.872, 14685.855, 16764.978, 17416.076
        ,20714.581, 21688.947]
fig, ax = plt.subplots()
plt.title('Динамика госдолга по годам(2010-2024)')
plt.xlabel("Год")
plt.ylabel("Размер долга(млрд.руб.)")

plt.xticks(rotation="vertical")
ax.plot(markers, data, '-bo', linewidth=2, markersize=6, markerfacecolor='black')

ax.grid()
plt.show()
