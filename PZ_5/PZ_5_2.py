"""
Описать функцию DigitCountSum(K, C, S), находящую количество С цифр целого положительного числа K, а также их сумму S
(K - входной, С и S - выходные параметры целого типа). С помощью этой функции найти количество и сумму цифр для каждого
из пяти данных целых чисел
"""


def digitcountsum(k):
    c = len(str(k))
    s = 0
    for u in range(c):
        s += k % 10
        k //= 10
    return c, s


for i in range(1, 6):
    while True:
        try:
            a = int(input(f'введите {i} число (целое положительное) >> '))
            if a > 0:
                break
            else:
                print('число должно быть целым положительным!\n')
        except ValueError:
            print('число должно быть целым положительным!\n')
    b, d = digitcountsum(a)
    print(f'количество цифр числа {b}, сумма цифр числа {d}\n')
