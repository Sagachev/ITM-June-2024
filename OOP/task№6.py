# В классе Car добавьте переменную класса car_drive = 4 и реализуйте classmethod, который выводит на экран переменну car_drive
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
    car_drive = 4
    def __init__(self, brand, color, wheels):
        super().__init__(brand, color)
        self.wheels = wheels

    def show_wheel(self):
        return print(f"Количество колес: {self.wheels}")
    @classmethod
    def show_car_drive(cls):
        print(f'значение car drive={cls.car_drive}')


car1 = Car("Red","BMW",4)
car1.show_car_drive()