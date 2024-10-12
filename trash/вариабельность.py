import statistics
x = [1,2]
#среднее
def mean(x):
    return sum(x)/len(x)

#дисперсия
def disp(x):
    result = 0
    meant = mean(x)
    for i in x:
        result += (i - meant) * (i - meant)

    return result/(len(x)-1)

#стандартное отклонение
def stdev1(x):
    return disp(x) ** 0.5


print(stdev1(x))
