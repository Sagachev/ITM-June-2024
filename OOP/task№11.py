# Реализуйте абстрактный класс Animals, создайте класс Cat, который будет наследоваться от класса Animals и реализуйте метод voice.
from abc import ABC, abstractmethod

class Animals(ABC):
    @abstractmethod
    def voice(self):
        pass

class Cat(Animals):
    def voice(self):
        print("Meow")

cat = Cat()
cat.voice()