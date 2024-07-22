# Создайте класс MeansOfTransport }}(для определения цвета и марки машины),
# принимающий 2 аргумента при инициализации (марка и цвет транспортного средства).
# В этом классе реализуйте методы {{show_color(),
# выводящий на печать цвет транспортного средства и show_brand, для получения марки транспортного средства.
class MeansOfTransport:
    def __init__(self, color, brand):
        self.__color = color
        self.__brand = brand
    def show_color(self):
        print(f"The color is {self.color}")
    def show_brand(self):
        print(f"The brand is {self.brand}")

car = MeansOfTransport("Black", "Renault")
car.show_color()
car.show_brand()



