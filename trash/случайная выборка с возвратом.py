import random


x = [1,2,3,4,5]
y = []
n = 3

i = 0

while i < n:
    y.append(x[random.randint(0,len(x)-1)])
    i+=1


print(y)
print(x)

