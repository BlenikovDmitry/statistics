import numpy as np



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

