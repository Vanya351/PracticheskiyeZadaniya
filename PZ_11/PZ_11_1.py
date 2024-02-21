"""
Средствами языка Python сформировать текстовый файл (.txt), содержащий последовательность из целых положительных и
отрицательных чисел. Сформировать новый текстовый файл следующего вида, предварительно выполнив требуемую обработку
элементов:
Исходные данные:
Количество элементов:
Сумма элементов:
Элементы, умноженные на минимальный элемент
"""

import random

lst = [random.randint(1, 20) for _ in range(random.randint(4, 10))]
for i in range(1, len(lst), 2):
    lst[i] *= -1

f = open('first.txt', 'w', encoding='utf-8')
for i in lst:
    f.write(str(i)+' ')
f.close()

f = open('first.txt', 'r', encoding='utf-8')
lst = f.read().split()
d = len(lst)
for i in range(d):
    lst[i] = int(lst[i])
f.close()

f = open('second.txt', 'w', encoding='utf-8')
f.write('Исходные данные:')
s = 0
m = min(lst)
for i in lst:
    f.write(' '+str(i))
    s += i

f.write('\nКоличество элементов: '+str(d))
f.write('\nСумма элементов: '+str(s))
f.write('\nЭлементы, умноженные на минимальный элемент:')
for i in range(d):
    f.write(' '+str(lst[i] * m))
