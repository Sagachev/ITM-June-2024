# #Напишите программу для подсчета среднего числа всех введенных пользователям чисел. Ввод пользователя должен осуществляться с помощью input.
# # Если пользователь вводит ноль, то выводиться на экран среднее значение. Используйте цикл while для решения данной задачи
total = 0
count = 0
while True:
    num = float(input("Введите число (или 0 для завершения): "))
    if num == 0:
        break
    total += num
    count += 1
if count > 0:
    average = total / count
    print(f"Среднее значение: {average:.2f}")
else:
    print("Вы не ввели ни одного числа.")

# #Напишите программу для вывода на экран чисел от 0 до 100
for i in range(101):
    print(i)

# #Напишите программу для вывода таблицы умножения от 0 до 9.
# #Используйте вложенный цикл for, print и range
# # Пример:
# # 0*1 = 0
# # 0 *2 = 0
# # …..
# # 9*1 = 9
# # 9*2=18
for i in range(10):
    for j in range(10):
        print(f"{i}*{j} = {i*j}")
    print()

# #Создайте список с разными значениями, пройдитесь по нему в цикле и выведите на экран. (Сделайте тоже самое со словарем и выведите ключ и значение)
fruits = ['apple', 'banana', 'cherry', 'kiwi', 'melon']
for fruit in fruits:
    print(fruit)


person = {'name': 'John', 'age': 30, 'city': 'New York'}
for key, value in person.items():
    print(f"Key: {key}, Value: {value}")

# #Вывести все числа от 1 до 100, которые делятся на 3 без остатка
for i in range(1, 101):
    if i % 3 == 0:
        print(i)

#Найти сумму всех чисел от 1 до 100
total_sum = 0
for i in range(1, 101):
    total_sum += i
print(total_sum)

# #Вывести таблицу умножения для числа 2 от 1 до 10.
for i in range(1, 11):
    print(f"2 x {i} = {2 * i}")
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

prime_numbers = []
for i in range(2, 51):
    if is_prime(i):
        prime_numbers.append(i)
print(prime_numbers)
#
# #Посчитать сумму квадратов чисел от 1 до 10.
total_sum = 0
for i in range(1, 11):
    total_sum += i ** 2
print(total_sum)
#
# # Вывести значения функции y=x^2 от 1 до 10 с шагом 0.
for x in range(1, 11, 1):
    for i in range(0, 11, 2):
        y = x ** 2
        print(f"x = {x + i / 10}, y = {y:.2f}")

# # Найти факториалы чисел от 1 до 5 (включительно).
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
for i in range(1, 6):
    print(f"Factorial of {i} is {factorial(i)}")

