# Дан словарь с произвольным количеством элементов. Выяснить имеется ли в нём элемент с ключом <<фрукт = яблоко>> и если
# он отсутствует, то добавить его в словарь. Вывести на экран первоначальный словарь и изменённый.

from random import randint

a = {}
d = [['ягода', 'орех', 'овощ', 'зелень', 'фрукт'], ['вишня', 'фундук', 'огурец', 'укроп', 'яблоко']]
for i in range(randint(1, 5)):
    a[d[0][i]] = d[1][i]

print('начальный', a)

if 'фрукт' not in a or a['фрукт'] != 'яблоко':
    a['фрукт'] = 'яблоко'

print('итоговый ', a)
