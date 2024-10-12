
x = [1,2,3,4,5,6,7,8,9]
w = [10,1,1,1,1,1,1,1,1]
'''
среднее арифметическое
'''
mean = sum(x) / len(x)

print(mean)
'''
среднее взвешенное
'''
sum_w = 0
i = 0
while i < len(x):
    sum_w += x[i] * w[i]
    i+=1
    
mean_wei = sum_w/ len(x)

print(mean_wei)

'''
медиана
!!!данные должны быть отсортированыы
'''
if len(x)%2 == 0:
    index1 = int(len(x) / 2)
    index2 = int((len(x) / 2) + 1)
    print((x[index1] + x[index2]) / 2)
else:
    print(x[int(len(x) / 2)])
