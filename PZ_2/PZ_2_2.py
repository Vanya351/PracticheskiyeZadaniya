# Вариант 15
# Известно, что Х кг шоколадных конфет стоит А рублей, а Y кг ирисок стоит В рублей.
# Определить, сколько стоит 1 кг шоколадных конфет, 1 кг ирисок, а также во сколько раз шоколадные конфеты дороже

while True:
    try:
        x = abs(float(input("введите Х (кг шоколадных конфет) >> ")))
        a = abs(float(input("введите A (стоимость Х кг) >> ")))
        y = abs(float(input("введите Y (кг ирисок) >> ")))
        b = abs(float(input("введите B (стоимость Y кг) >> ")))

        s1 = round(a / x, 3)
        s2 = round(b / y, 3)
        s3 = round(s1 / s2, 3)
        break
    except ValueError:
        print("Вводить надо число!\n")
    except ZeroDivisionError:
        print("Нельзя ввести 0 кг!\n")


print("\nстоимость 1 кг шоколадных конфет: ", s1)
print("стоимость 1 кг ирисок: ", s2)
print("шоколадные конфеты дороже ирисок в ", s3, " раз")
