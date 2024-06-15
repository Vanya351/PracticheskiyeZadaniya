"""
Создать класс Person с одним аттрибутом (count), с конструктором __init__ и одним статическим методом
Увеличение количества созданных экземпляров обеспечить в конструкторе __init__
Статический метод total_people должен обеспечивать построение и вывод фразы о количестве созданных экземпляров
"""


class Person:
    count = 0

    def __init__(self, s, age):
        self.s = s
        self.age = age
        Person.count += 1

    @staticmethod
    def total_people():
        print("Создано эксземпляров", Person.count)


man1 = Person("man", 43)
man2 = Person("man", 20)
wooman1 = Person("woman", 23)

Person.total_people()
