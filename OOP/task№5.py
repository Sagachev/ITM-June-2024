# Реализуйте два класса Car и Moped, которые будут наследоваться от класса MeansOfTransport.
# При инициализации они должны принимать новый аргументы(количество колес.
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

class Car(MeansOfTransport):
    def __init__(self, color, brand, wheels):
        super().__init__(color, brand)
        self.__wheels = wheels

    def show_wheels(self):
        print(f"Количество колес: {self.__wheels}")

    @property
    def wheels(self):
        return self.__wheels

    @wheels.setter
    def wheels(self, wheels):
        self.__wheels = wheels

class Moped(MeansOfTransport):
    car_drive = 4
    def __init__(self, color, brand, wheels):
        super().__init__(color, brand)
        self.__wheels = wheels

    def show_wheels(self):
        print(f"Количество колес: {self.__wheels}")

    @property
    def wheels(self):
        return self.__wheels

    @wheels.setter
    def wheels(self, wheels):
        self.__wheels = wheels

car = Car("Black", "Renault", 4)
car.show_color()
car.show_brand()
car.show_wheels()

moped = Moped("Red", "BMW", 2)
moped.show_color()
moped.show_brand()
moped.show_wheels()

