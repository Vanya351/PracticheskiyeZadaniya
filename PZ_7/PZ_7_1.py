# Дано целое число N (1 < N < 26). Вывести N первых прописных (то есть заглавных) букв латинского алфавита

al = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

while 1:
    try:
        n = int(input("N, сколько букв вывести? (1 < N < 26) >> "))
        if 1 < n < 26:
            break
        else:
            print('N должно быть не меньше двух и не больше двадцати пяти!\n')
    except ValueError:
        print('N должно быть целым числом!\n')

print(f'первые {n} букв: {al[:n]}')
