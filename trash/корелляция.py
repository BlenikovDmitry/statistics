import statistics

x = [1,2]
y = [1,2]

#среднее
def mean(x):
    return sum(x)/len(x)

#стандартное отклонение
def stdev1(x):
    return disp(x) ** 0.5

#дисперсия
def disp(x):
    result = 0
    meant = mean(x)
    for i in x:
        result += (i - meant) * (i - meant)

    return result / (len(x)-1)

def upper_var(x,y):
    mean_x = 0
    mean_y = 0
    mean_x = mean(x)
    mean_y = mean(y)
    sums = 0
    i = 0
    while i < len(x):
        sums += (x[i] - mean_x) * (y[i] - mean_y)
        i+=1

    return sums

stdev_x = stdev1(x)
stdev_y = stdev1(y)


result = upper_var(x,y) / ((len(x)-1) * stdev_x * stdev_y)

'''r = statistics.correlation(x, y)'''
print(result)
#print(r)
