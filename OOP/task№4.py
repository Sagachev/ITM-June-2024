# Работаем с классом из 3 пункта. Реализуйте сеттеры и геттеры для цвета и марки транспортного средства.
class MeansOfTransport:
    def __init__(self, color, brand):
        self.__color = color
        self.__brand = brand

    def show_color(self):
        print(f"Цвет транспортного средства: {self.__color}")

    def show_brand(self):
        print(f"Марка транспортного средства: {self.__brand}")

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, brand):
        self.__brand = brand

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color


car = MeansOfTransport('Black', 'Renault')
car1 = MeansOfTransport('white', 'lt')
car.show_color()
car.show_brand()
car1.show_color()
car1.show_brand()
