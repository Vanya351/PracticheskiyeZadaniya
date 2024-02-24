# В матрице элементы второго столбца возвести в квадрат

from random import randint

r = randint(2, 10)
m = [[randint(-10, 10) for _ in range(r)] for __ in range(randint(2,10))]

print('матрица до преобразования')
for i in m:
    print(i)

m = [[m[i][u] if u != 1 else m[i][u] ** 2 for u in range(r)] for i in range(len(m))]

print('\nконечная матрица')
for i in m:
    print(i)
