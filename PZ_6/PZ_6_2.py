# Дан список А размера N и целые числа K и L (1 < K < L < N). Переставить в обратном порядке элементы списка,
# расположенные между элементами А(K) и A(L), включая эти элементы

from random import randint

a = []
while 1:
    try:
        n = int(input("N, сколько элементов будет в списке? (минимум 4) >> "))
        if n < 4:
            print('N должно быть не меньше пяти!\n')
        else:
            break
    except ValueError:
        print('N должно быть целым числом!\n')

for i in range(n):
    a.append(randint(-10, 10))
    # a.append(i)

while 1:
    try:
        k = int(input("K, диапозон переставки, от какого элемента? (минимум 2) >> "))
        if (k < 2) or (k > (n - 2)):
            print('K должно быть не меньше двух и не больше N - 2!\n')
        else:
            k -= 1
            break
    except ValueError:
        print('K должно быть целым числом!\n')

while 1:
    try:
        L = int(input("L, диапозон переставки, до какого элемента? (больше k, меньше N) >> "))
        if L <= k or (L > (n - 1)):
            print('L должно быть больше K и меньше N!\n')
        else:
            L -= 1
            break
    except ValueError:
        print('L должно быть целым числом!\n')

print('\nизначальный список\n', a, sep='')

while k <= L:
    a[k], a[L] = a[L], a[k]
    k += 1
    L -= 1

print('\nпереставленный список\n', a, sep='')
