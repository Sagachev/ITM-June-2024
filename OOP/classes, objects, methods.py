# Имя класса начинать с заглавной буквы
class Point:
#     "Класс для представления координат точек на плоскости"
#     # Переменные внутри класса называют атрибутами класса или его свойствами
#     color = "red"
#     circle = 2
# pt = Point() # Создание нового объекта класса Point
# getattr(Point, 'color') # = ( red ) Возвращает значение атрибута объекта
# hasattr(Point, 'color') # = ( True ) Проверяет на наличие атрибута в объекте
# setattr(Point, 'type', 4) # = (type = 4) задает значение атрибута, если атрибут не существует, то он создается)
# delattr(Point, 'type') # = Удаляет атрибут с именем type
#
# Point.__doc__ # Содержит строку с описанием класса = строка №3 "Класс для представления координат точек на плоскости"
# Point.__dict__ # Содержит набор атрибутов экземпляра класса.

    def __init__(self, x, y):
        # print("вызов __init__")
        self.x = x
        self.y = y
    def set_coords(self, x, y): #  self - это параметр метода, который ссылается на экземпляр класса, для которого вызывается метод
        self.x = x
        self.y = y

pt = Point(1, 2)
print(pt.__dict__)



