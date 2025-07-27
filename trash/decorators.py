
'''
типичный синтаксис декоратора
передаем функцию, из которой в обертке получаем результат
и модифицируем его по своему усмотрению. не меняя код исходной функции
'''
def some_decorator(func):
    def wrapper():
        original_result = func()
        modified_result = original_result + 1
        return modified_result
    return wrapper

'''
декоратор к функции инкремента
проверяет делится ли число на 2
'''
def logging(func):
    def wrapper():
        original_result = func()
        if original_result % 2 == 0:
            modified_result = 'делится на 2: ' + str(original_result)
        else:
            modified_result = 'не делится на 2: ' + str(original_result)
                
        return modified_result
    return wrapper

'''
пример использования декоратора
пишем функцию инкремента, но с декоратором инкремент будет на 2 единицы
вместо 1
если применить несколько декораторов, они применятся снизу вверх
'''
@logging
def incr():
    return i + 1

i = 0
while i < 10:
    print(incr())
    i += 5

#print(some_decorator(greet))

