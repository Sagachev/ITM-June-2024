# Механизм инкапсуляции
# x (без подчеркиваний в начале) - публичное свойство
# _x (с одним подчеркиванием) - режим доступа protected - служит для обращения внутри класса и во всех его дочерних классах)
# __x ( с двумя подчеркиваниями) - режим доступа private - служит для обращения только внутри класса
# Более надежная защита с помощью модуля accessify, но она используется редко
class Point:

    def __init__(self, x=0, y=0):
        self.__x = self.__y = 0
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y
    @classmethod
    def __check_value(cls, x):
        return type(x) in (int, float)

    def set_coord(self, x, y):#сеттер
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError("Координаты должны быть числами")
    def get_coord(self): #геттер
        return self.__x, self.__y
pt = Point(1,2)
pt.set_coord(10, 20)
print(pt.get_coord())
