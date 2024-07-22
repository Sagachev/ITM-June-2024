# Реализуйте класс Dog. Придумайте, какие переменные будет принимать данный класс и какие методы будут реализованы.
# Реализуйте в этом классе паттерн Singleton
class Dog:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Dog, cls).__new__(cls)
        return cls._instance

    def __init__(self, name, age):
        self.name = name
        self.age = age

dog1 = Dog("Buddy", 5)
dog2 = Dog("Max", 3)
print(dog1 is dog2)  # True