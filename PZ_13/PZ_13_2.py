# Сгенерировать матрицу, в которой нечётные элементы заменяются на 0

from random import randint

r = randint(2, 10)
m = [[randint(-10, 10) for _ in range(r)] for __ in range(randint(2,10))]

print('матрица до преобразования')
for i in m:
    print(i)

for x in range(len(m)):
    for y in range(len(m[0])):
        if m[x][y] % 2 == 1:
            m[x][y] = 0

print('\nконечная матрица')
for i in m:
    print(i)
