"""
Задание 2
1. Создайте класс Image
2. У каждого экземпляра класса должно быть три собственных аттрибута: resolution, title, extension
3. В классе должен быть метод resize, с помощью которого можно поменять разрешение изображения
4. В классе должен быть метод title_upper, с помощью которого можно имя файла записать в верхнем регистре
5. Создайте несколько экземляров класса Image и вызовите для каждого метод resize
"""


class Image:
    def __init__(self, resolution: [int, int], title: str, extension: str):
        self.resolution = resolution
        self.title = title
        self.extension = extension

    def resize(self, width, height):
        self.resolution = [width, height]

    def title_upper(self):
        self.title = self.title.upper()


image1 = Image([1920, 1080], title="picture", extension=".png")
image2 = Image([3840, 2160], title="photo", extension=".jpg")
image3 = Image([640, 480], title="screenshot", extension=".bmp")

image1.resize(1280, 720)
image2.resize(15360, 8640)
image3.resize(160, 120)

image1.title_upper()
print(image1.__dict__)
print(image2.__dict__)
print(image3.__dict__)
