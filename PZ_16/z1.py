"""
Задание 1
Изменить конструктор класс Note, добавив атрибут iscompleted (True/False)
Создать экзмепляр с новым атрибутом, вывести все значения собственных атрибутов экземпляра (__dict__)
Обеспечить увеличение count на величину, передаваемую в качестве аргумента
Создать новую функцию reset_count, которая будет обнулять счётчик выполненных задач
Проверить содержимое магической переменной __dict__
"""


class Note:
    def __init__(self, text, compl: bool):
        self.text = text
        self.iscompleted = compl
        self.count = 0

    def upcount(self, size):
        self.count += size

    def reset_count(self):
        self.count = 0


n1 = Note('Задание 1', False)
print(n1.__dict__)

n1.upcount(3)
print(n1.__dict__)

n1.reset_count()
print(n1.__dict__)
