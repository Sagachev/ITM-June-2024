# Написать программу на Python для решения квадратного уравнения ax^2 + bx + c = 0.
# Если дискриминант отрицателен, программа должна выдать ошибку и предложить пользователю попробовать еще раз с другими коэффициентами.
# При выполнении скрипта в лог должна записываться информация о успехе или неудаче операции.
import math
import logging

#Настройка логирования
logging.basicConfig(filename='quadratic_equation.log', level=logging.INFO, format='%(asctime)s - %(message)s')

#Определение функции для создания уравнения
def solve_quadratic_equation(a, b, c):
    discriminant = b**2 - 4*a*c
#Проверка условия, если дискриминант отрицательный, записываем ошибку в лог и выводим ошибку на экран
    if discriminant < 0:
        logging.error("Дискриминант отрицательный. Уравнение не имеет действительных корней.")
        print("Ошибка: Дискриминант отрицательный. Попробуйте другие коэффициенты.")
        return None
#Вычисление корней
    x1 = (-b + math.sqrt(discriminant)) / (2*a)
    x2 = (-b - math.sqrt(discriminant)) / (2*a)
#Запись успешного решения уравнения в лог
    logging.info(f"Корни уравнения: x1 = {x1}, x2 = {x2}")

    return x1, x2

a = float(input("Введите коэффициент a: "))
b = float(input("Введите коэффициент b: "))
c = float(input("Введите коэффициент c: "))
#Вызов функции
result = solve_quadratic_equation(a, b, c)
if result:
    print("Корни уравнения:", result)
