# Дано целое число N (>0). Используя операции деления нацело и взятия остатка от деления,
# найти количество и сумму его цифр

while 1:
    try:
        n = int(input("введите N (целое число, >0) >> "))
        print("\nваше число =", n)
        if n <= 0:
            print("\nN > 0!\n")
        else:
            break
    except ValueError:
        print("n должно быть числом!\n")

a, i = 0, 0

while n != 0:
    a += n % 10
    n //= 10
    i += 1

print("сумма цифр числа =", a, "\nколичество цифр числа = ", i)
