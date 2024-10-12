import matplotlib.pyplot as plt

'''
Простой пример диаграммы рассеяния
'''
x = [1,2,3,4]
y = [-1,-2,-3,-4]

plt.title("Диаграмма рассеяния(продажи)")
plt.xlabel("Шиндовс")
plt.ylabel("Открытые системы")
plt.scatter(x,y, marker="o", c = "#2ca02c")

plt.grid()
plt.show()
