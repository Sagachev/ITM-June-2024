# __setattr__(self, key, value) - автоматически вызывается при изменении свойства key класса
# __getattrшигеу__(self, item) - автоматически вызывается при получении свойства класса с именем item
# __getattr__(self, item) - автоматически вызывается при получении несуществующего свойства item класса
# __delattr__(self, item) - автоматически вызывается при удалении свойства item (не важно, существует он или нет)
class Point:
    MAX_CORD = 100
    MIN_CORD = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def set_coord(self, x, y):
        if self.MIN_COORD <= x <= self.MAX_COORD:
            self.x = x
            self.y = y

    def __getattr__(self, item):
        return False
    def __delattr__(self, item):
        print("__delattr__:" + item)

pt1 = Point(1,2)
pt2 = Point(10,20)
print(pt1.MAX_CORD)
