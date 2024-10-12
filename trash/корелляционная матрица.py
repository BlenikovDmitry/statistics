import statistics

'''
строит простейшую корелляционную матрицу
'''
x = [[1,2,3], [10,5,1], [7,8,9]]
y = [[0,0,0], [0,0,0], [0,0,0]]
z = ["F", "S", "T"]


i = 0
j = 0

while i < len(x):
    j = 0
    while j < len(x):
        y[i][j] = statistics.correlation(x[i], x[j])
        y[i][j] = round(y[i][j], 2)
        j+=1
    i+=1


print(z)
i = 0
while i < len(x):
    print(z[i], "", y[i])
    i+=1
