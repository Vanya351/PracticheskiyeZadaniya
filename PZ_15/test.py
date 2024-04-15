import pymysql

connection = pymysql.connect(
    host="localhost",
    port=3306,
    user="training",
    password="adfhiu1839",
    database="oaip",
)

with connection.cursor() as cursor:
    cursor.execute("DROP TABLE IF EXISTS users;")
    cursor.execute("CREATE TABLE IF NOT EXISTS users("
                   "user_id INT PRIMARY KEY AUTO_INCREMENT, "
                   "name TEXT NOT NULL, "
                   "sex INT NOT NULL DEFAULT 1, "
                   "old INT, "
                   "score INT);")

with connection.cursor() as cursor:
    cursor.execute("INSERT INTO users VALUES(1, 'Алексей', 1, 22, 1000);")

with connection.cursor() as cursor:
    cursor.execute("SELECT * FROM users;")
    print(cursor.fetchall())
