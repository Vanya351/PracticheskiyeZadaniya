# Дан список размера N. Обнулить все его локальные максимумы (то есть числа, большие своих соседей)

from random import randint

a, b = [], []
while 1:
    try:
        n = int(input("N, сколько элементов будет в списке? >> "))
        break
    except ValueError:
        print('N должно быть целым числом!\n')

for i in range(n):
    a.append(randint(-10, 10))
    b.append(0)

print('\nизначальный список\n', a, sep='')

if len(a) == 1:
    a[0] = 0
else:
    for i in range(len(a)):
        if 0 < i < (len(a) - 1):
            if (a[i] > a[i - 1]) and (a[i] > a[i + 1]):
                b[i] = 1
        elif i == 0:
            if a[i] > a[i + 1]:
                b[i] = 1
        else:
            if a[i] > a[i - 1]:
                b[i] = 1

    for i in range(len(a)):
        if b[i] == 1:
            a[i] = 0

print('\nитоговый список\n', a, sep='')
