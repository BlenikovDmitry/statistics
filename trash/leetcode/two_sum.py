
'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
'''
nums = [3,3]
target = 6

'''
пишем через словарь
1) записываем в словарь все числа подряд из nums и их индексы
ключ = число
значение = список индексов
важно! если числа там еще нет - делаем его ключом, создаем под него пустой список индексов и заполняем его

2) идем по списку nums, считаем разницу между target и текущим элементом списка nums
чтобы получить пару значений, которые в сумме дают target
если эта разница есть в словаре - существует такой ключ, то бкркм все его индексы и пишем пару : текущий индекс в массиве nums и найденные в словаре по ключу comp
ind > i чтобы мы не взяли элемент дважды
'''
res = []
index_map = dict()
count = 0
for i, num in enumerate(nums):
    if num not in index_map:
        index_map[num] = []
    index_map[num].append(i)
#выводим для самопроверки


print(index_map)

for i, num in enumerate(nums):
    comp = target - num
    if comp in index_map:
        for ind in index_map[comp]:
            if ind > i:
                res.extend([i,ind])

print(res)


