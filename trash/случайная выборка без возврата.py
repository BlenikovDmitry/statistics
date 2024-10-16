import random


x = [1,2,3,4,5]
y = []
n = 3

i = 0
index = 0

while i < n:
    index = random.randint(0,len(x)-1)
    y.append(x[index])
    x.remove(x[index])
    i+=1


print(y)
print(x)
