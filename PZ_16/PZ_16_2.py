# Создайте класс Фрукт, который содержит информацию о наименовании и весе фрукта. Создайте классы Яблоко и Апельсин,
# которые наследуются от класса Фрукт и содержат информацию о цвете

class Fruit:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.color = None

    def get_information(self):
        print(f'название {self.name}, вес {self.weight}{", цвет " + self.color if self.color is not None else ""} ')


class Apple(Fruit):
    def __init__(self, weight, color):
        super().__init__('Яблоко', weight)
        self.color = color


class Orange(Fruit):
    def __init__(self, weight, color):
        super().__init__('яблоко', weight)
        self.color = color


banana = Fruit('банан', 10)
apple = Apple('24', 'красный')
orange = Orange('13', 'оранжевый')

banana.get_information()
apple.get_information()
orange.get_information()
