# Написать программу для нахождения среднего арифметического списка чисел.
# Если при вводе списка чисел была допущена ошибка (например, был передан не список, а строка), программа должна корректно обработать эту ошибку и выдать соответствующее сообщение.
# Информация об ошибках должна быть записана в лог.

import logging

logging.basicConfig(filename='calculate_average.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

def calculate_average(numbers):
    try:
        if not isinstance(numbers, list):
            raise TypeError("Аргумент должен быть списком")
        return sum(numbers) / len(numbers)
    except TypeError as e:
        logging.error(f"Ошибка: {e}")
        print(f"Ошибка: {e}. Пожалуйста, введите список чисел.")
        return None
    except ZeroDivisionError:
        logging.error("Ошибка: список пустой")
        print("Ошибка: список пустой. Пожалуйста, введите ненулевой список чисел.")
        return None

# Пользовательский ввод
while True:
    try:
        user_input = input("Введите список чисел, разделенных пробелами: ")
        numbers = [float(num) for num in user_input.split()]
        average = calculate_average(numbers)
        if average is not None:
            print(f"Среднее арифметическое: {average:.2f}")
        break
    except ValueError:
        logging.error("Ошибка: неверный ввод данных")
        print("Ошибка: неверный ввод данных. Пожалуйста, введите корректные числа.")