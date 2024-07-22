# Попробуйте инициализировать несколько любых переменных в классе Car и сделайте одну переменную приватной,
# одну защищенной. Попробуйте получить к ним доступ. Какой результат
# В классе {{Moped}}напишите статическую функцию, которая на вход будет принимать расстояние и максимальную скорость,
# а на выходе получать время, за которое проедет мопед это расстояние.
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
    def __init__(self, brand, color, wheels):
        super().__init__(brand, color)
        self.wheels = wheels
        self.__private_call = 'она приватная'
        self._secure_call = 'она защищенная'
        self.public_call = 'она общедоступная'
    def show_wheel(self):
        return print(f"Количество колес: {self.wheels}")




car1 = Car("Red","BMW",4)
print(car1._Car__private_call)
#print(car1.__private_call)
print(car1.public_call)
print(car1._secure_call)