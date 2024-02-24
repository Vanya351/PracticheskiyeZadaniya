# В матрице элементы второго столбца возвести в квадрат

from random import randint

r = randint(2, 10)
m = [[randint(-10, 10) for _ in range(r)] for __ in range(randint(2,10))]

print('матрица до преобразования')
for i in m:
    print(i)

for i in range(len(m)):
    m[i][1] **= 2

print('\nконечная матрица')
for i in m:
    print(i)
