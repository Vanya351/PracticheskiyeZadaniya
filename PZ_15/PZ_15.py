"""
Реализовать программу для работы с однотабличной БД. Программа должна обеспечивать функционал по вводу данных в БД,
их поиску, удалению и редактированию. При организации поиска, удаления и редактирования использовать WHERE,
предусмотреть по три SQL-запроса для каждой операции. Приложение БАНК для отслеживания накапливаемых на счетах
клиентов банка сумм: Таблица Клиент должна содержать следующую информацию: Код клиента, Клиент (Ф.И.О.), Периодический
платёж, Годовой %, Срок вклада, Пластиковая карта (логическое поле), Конечная сумма.
"""

import pymysql


def inpution(s: str, t: int, d=''):
    n = ''
    while n == '':
        n = input(f'{s} ({d}) >> ')
        if t >= 1 and n == '':
            print(s, 'не может быть пустым\n')
        if t == 2 and n != '':
            try:
                float(n)
            except ValueError:
                print(s, 'должно быть числом\n')
        elif t == 3 and n != '':
            if n == 't':
                n = True
            elif n == 'f':
                n = False
            else:
                n = ''
    return n


connection = pymysql.connect(
    host="localhost",
    port=3306,
    user="training",
    password="adfhiu1839",
    database="oaip",
)

with connection.cursor() as cursor:
    cursor.execute("CREATE TABLE IF NOT EXISTS clients ("
                   "code INT PRIMARY KEY AUTO INCREMENT,"
                   "name VARCHAR(32) NOT NULL,"
                   "sname VARCHAR(32) NOT NULL,"
                   "fname VARCHAR(32),"
                   "pay DECIMAL(12,2) NOT NULL,"
                   "percent DECIMAL(5,2) NOT NULL,"
                   "period INT NOT NULL,"
                   "card BOOL NOT NULL,"
                   "final DECIMAL (14,2));")

while True:
    print('\n'*30)
    print('Выберите опцию вводом соответствующей цифры или названия')
    v = input('1. Ввод, 2. Поиск, 3. Удаление, 4. Редактирование\n>> ')
    if v == '1' or v == 'Ввод':
        name = inpution('имя клиента', 1)
        sname = inpution('фамилия', 1)
        fname = inpution('отчество', 0, 'если нет просто нажмите enter')
        pay = inpution('периодический платёж', 2)
        percent = inpution('годовой процент', 2)
        period = inpution('срок вклада', 2)
        card = inpution('имеется ли карта', 3, 't/f')
        final = inpution('конечная сумма', 2, 'введите -1 для авторасчёта')


'''
with connection.cursor() as cursor:
    cursor.execute("SELECT id_u FROM users WHERE id_u='" + str(user_id) + "'")
    rows = cursor.fetchall()
    if rows == ():
        insert_query = "INSERT INTO users (id_u, role, rep) VALUES ('" + str(user_id) + "', 0, 0);"
        cursor.execute(insert_query)
        role = 0
        connection.commit()
    else:
        cursor.execute("SELECT role FROM users WHERE id_u='" + str(user_id) + "'")
        rows = cursor.fetchall()
        role = rows[0][0]
'''