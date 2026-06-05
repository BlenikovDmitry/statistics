import numpy as np
import matplotlib.pyplot as plt



'''
Функция быстрого бутстрапа
достигается с помощью numpy, а именно последовательного хранения в памяти
и групповых операций
'''
def bootstrap(data, iterations):
    stats_average = np.zeros(iterations)
    stats_std = np.zeros(iterations)
    tmp = np.zeros(len(data))
    rng = np.random.default_rng()
    for i in range(iterations):
        tmp = rng.choice(data, size=len(data), replace=True)
        stats_average[i] = tmp.mean()
        stats_std[i] = tmp.std()
    return stats_average, stats_std



tmp = [1,2,3,4]
data = np.array(tmp, dtype = np.float32)

stats_average, stats_std = bootstrap(data, 10000000)

fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot(2,1,1)
ax.set_title("Распределение среднего")
ax.hist(stats_average, 50, color = "red", ec="lightblue", edgecolor="black", rwidth = 5)
ax.grid()
    
ax = fig.add_subplot(2,1,2)
ax.set_title("Распределение стандартного отклонения")
ax.hist(stats_std, 50, color = "lightblue", ec="red", edgecolor="black", rwidth = 5)
ax.grid()

plt.show()
