# Написать программу для генерации случайных чисел в заданном диапазоне.
# Если пользователь ввел недопустимые границы диапазона (например, меньше нуля), программа должна вывести ошибку и попросить ввести диапазон заново.
# Информация об ошибках должна быть записана в лог.
import random
import logging
#Настройка логирования
logging.basicConfig(filename='number generator.log', level=logging.ERROR)

def generate_random_number():
#Начало бесконечного цикла пока не будут введены корректные числа диапазона
    while True:
        try:
            start = int(input("Введите начало диапазона: "))
            end = int(input("Введите конец диапазона: "))
            if start >= end:
                raise ValueError("Начало диапазона должно быть меньше конца диапазона")
            if start < 0 or end < 0:
                raise ValueError("Границы диапазона не могут быть отрицательными")
#Генерирует случайное
            random_number = random.randint(start, end)
            return random_number
        except ValueError as error:
            logging.error(f"Ошибка: {error}.")
            print(f"Ошибка: {error}. Пожалуйста, введите диапазон заново.")

random_number = generate_random_number()
print(f"Случайное число из заданного диапазона: {random_number}")