'''
задание аргументов функции по умолчанию
после первого аргумента по умолчанию, все остальные аргументы
становятся необязательными
'''
def func_default(i = 1, msg = 'hello', desc = 'агрументы по умолчанию' ):
    counter = 0
    print(desc)
    while counter < i:
        print(msg)
        counter += 1


params_cort = (1,2,3,4,5)
params_dict = {'first': '1', 'second': '2'}

'''
задание переменного количества аргументов
*args - кортеж аргументов
**kwargs - словарь аргументов
'''
def func_argc_kwargs(*args, **kwargs):
    print('переданные аргументы в кортеже')
    for item in args:
        print(item)
        
    print('переданные аргументы в словаре(передача позиционных именованных аргументов)')
    for item in kwargs:
        print(item + ":" + kwargs[item])

'''
но можно и без этого геморроя =))
просто передаем кортеж и словарь и не заморачиваемся
смысл использовать
*args - кортеж аргументов
**kwargs - словарь аргументов
есть
если передавать не отдельным кортежем и словарем, а прямо в функцию
'''
def func_none_packages(args, kwargs):
    print('переданные аргументы в кортеже')
    for item in args:
        print(item)
        
    print('переданные аргументы в словаре(передача позиционных именованных аргументов)')
    for item in kwargs:
        print(item + ":" + kwargs[item])

'''
пример функции с нормальным применением *args
'''
def func_unpack_cort(*args):
    print('переданные аргументы в кортеже')
    for item in args:
        print(item)
'''
пример функции с нормальным применением **kwargs
'''
def func_unpack_dict(**kwargs):
    print('переданные аргументы в кортеже')
    for item in kwargs:
        print("{} is {}".format(item, kwargs[item]))
    



'''func_default()
func_default(5, 'hello', 'аргументы передаются в функцию явно')'''

'''func_argc_kwargs(*params_cort, **params_dict)'''
'''func_none(params_cort, params_dict)'''

'''func_unpack_cort(1,2,3,4)'''
'''func_unpack_dict(first = 1, second = 2)'''
