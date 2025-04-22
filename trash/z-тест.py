import statistics

'''
Исходные данные и подготовка компонентов
'''
general = [1,2,3,4,5,6,7,8,10,10,11,12,13,14,15]
general2 = [1,2,3,4,5,6,7,8,10,10,11,12,13,14,15,16,17,18,19,20]

choose = [1,2,3,4,5]
choose2 = [10,11,12,13,14,15]



mean_general = statistics.mean(general)
mean_general2 = statistics.mean(general2)
mean_choose = statistics.mean(choose)
mean_choose2 = statistics.mean(choose2)
std_general = statistics.stdev(general)
disp_general = statistics.pvariance(general)


disp_general2 = statistics.pvariance(general2)

n = len(choose)
m = len(choose2)

'''
Одновыборочный z - тест
проверяет гипотезу что среднее выборки равно среднему ген совокупности
Если это так то результат будет лежать в диапазоне от -2  до 2 стандартных отклонений
можно еще ввести а(он же вероятность ошибки 1 рода) - доверительный интервал, обычно он 5%, тогда будет диапазон от -1,96 до 1,96
Практический пример: доходность выбранных облигаций отличается от индекса тех же самых бумаг
'''


z = (mean_choose - mean_general) / (std_general / (n ** 0.5))

print('одновыборочный z тест:' ,z)


'''
двухвыборочный z тест
выборки зависимы - из одной ген совокупности
сравниваем средние в выборках их одной совокупности
Практический пример: доходность выбранных облигаций не отличается от доходности пифов составленных из бумаг того же класса
'''

z = (mean_choose - mean_choose2 - (mean_general - mean_general) ) / (((disp_general * disp_general) / n + (disp_general * disp_general) / m) ** 0.5)

print('двухвыборочный зависимый z тест:', z)


'''
двухвыборочный z тест
выборки независимы - из разных ген совокупностей
сравниваем средние из разных совокупностей
Практический пример: доходность выбранных облигаций отличается от доходности акций
'''
z = (mean_choose - mean_choose2 - (mean_general - mean_general2)) / (((disp_general * disp_general) / n + (disp_general2 * disp_general2) / m) ** 0.5)
print('двухвыборочный независимый z тест:', z)
