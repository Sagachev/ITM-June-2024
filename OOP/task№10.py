# Реализуйте класс Calculator, в котором будет один метод, для вычисления суммы двух чисел.
class Calculator:
    def sum(self, a, b):
         return a + b


calculator = Calculator()

result = calculator.sum(9, 12)
print(result)

# Реализуйте еще один класс, который будет наследоваться от класса Calculator и перегрузите метод для вычисления суммы двух чисел,
# чтобы он делал конкатенацию двух строк.
class StringCalculator(Calculator):
    def sum(self, a, b):
        return str(a) + str(b)

string_calculator = StringCalculator()


result = string_calculator.sum("Hi, ", "Bro!")
print(result)