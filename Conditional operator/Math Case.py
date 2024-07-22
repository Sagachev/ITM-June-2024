#1 Дано целое число K. Вывести строку-описание оценки, соответствующей числу K (1 — «плохо», 2 — «неудовлетворительно», 3 — «удовлетворительно», 4 — «хорошо», 5 — «отлично»). Если K не лежит в диапазоне 1–5, то вывести строку «ошибка».

k = int(input("Введите целое число K: "))
match k:
    case 1:
        print("плохо")
    case 2:
        print("неудовлетворительно")
    case 3:
        print("удовлетворительно")
    case 4:
        print("хорошо")
    case 5:
        print("отлично")
    case _:
        print("ошибка")

#	Дан номер месяца — целое число в диапазоне 1–12 (1 — январь, 2 — февраль и т. д.). Определить количество дней в этом месяце для невисокосного года.

month = int(input("Введите номер месяца: "))
match month:
    case 1 | 3 | 5 | 7 | 8 | 9 | 10 | 12:
        print("31")
    case 2:
        print("29")
    case 4, 6, 11:
        print("30")

    case _:
        print("ошибка")


from datetime import datetime, timedelta

def next_date(day, month):
    match month:
        case 1 | 3 | 5 | 7 | 8 | 10:
            if day == 31:
                return 1, (month % 12) + 1
            else:
                return day + 1, month
        case 4 | 6 | 9 | 11:
            if day == 30:
                return 1, (month % 12) + 1
            else:
                return day + 1, month
        case 2:
            if day == 28:
                return 1, (month % 12) + 1
            else:
                return day + 1, month
        case 12:
            if day == 31:
                return 1, 1
            else:
                return day + 1, month
        case _:
            raise ValueError("Неправильный месяц")

# Ввод дня и месяца
D = int(input("Введите день: "))
M = int(input("Введите месяц: "))

# Получение следующей даты
next_day, next_month = next_date(D, M)

print(f"Следующая дата: {next_day} {next_month}")

#4.	Робот может перемещаться в четырех направлениях («С» — север, «З» — запад, «Ю» — юг, «В» — восток)
# и принимать три цифровые команды: 0 — продолжать движение, 1 — поворот налево, −1 — поворот направо.
# Дан символ C — исходное направление робота и целое число N — посланная ему команда.
# Вывести направление робота после выполнения полученной команды.
def path_robot():
    C = input("Введите исходное направление (С, З, Ю, В): ").upper()
    N = int(input("Введите команду (0 — продолжать движение, 1 — поворот налево, −1 — поворот направо): "))
    Direction = ["С", "В", "Ю", "З"]

    if C in Direction:
        index = Direction.index(C)
        match N:
            case 0:
                pass
            case 1:
                index = (index - 1) % 4
            case -1:
                index = (index + 1) % 4
            case _:
                print("Ошибка команды")
                return
        print(f"Новое направление: {Direction[index]}")
    else:
        print("Ошибка направления")

path_robot()

# 5.	Дано целое число в диапазоне 100–999. Вывести строку-описание данного числа, например: 256 — «двести пятьдесят шесть», 814 — «восемьсот четырнадцать».
def number_to_text(number):
    if not 100 <= number <= 999:
        return "Число должно быть в диапазоне от 100 до 999"

    ones = ["", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
    teens = ["", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать", "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать"]
    tens = ["", "десять", "двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят", "девяносто"]

    hundreds = number // 100
    tens_digit = (number % 100) // 10
    ones_digit = number % 10

    result = ""

    match hundreds:
        case 1:
            result += "сто "
        case 2:
            result += "двести "
        case 3:
            result += "триста "
        case 4:
            result += "четыреста "
        case 5:
            result += "пятьсот "
        case 6:
            result += "шестьсот "
        case 7:
            result += "семьсот "
        case 8:
            result += "восемьсот "
        case 9:
            result += "девятьсот "

    if tens_digit == 1 and ones_digit != 0:
        result += teens[ones_digit]
    else:
        result += tens[tens_digit]
        if ones_digit != 0:
            result += " " + ones[ones_digit]

    return result.strip()

user_input = int(input("Введите число от 100 до 999: "))
print(number_to_text(user_input))

#6 6.	*** Реализуйте программу калькулятор. На вход подается три значения: первое число, второе число и операция( *, /, + или -) .
# На выходе должны получить число, после выполнения операции.
def calculator(num1, num2, operation):
    match operation:
        case '+':
            return num1 + num2
        case '-':
            return num1 - num2
        case '*':
            return num1 * num2
        case '/':
            if num2 != 0:
                return num1 / num2
            else:
                return "Error: Division by zero"
        case _:
            return "Error: Invalid operation"

# Пример использования
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
operation = input("Введите операцию (+, -, *, /): ")

result = calculator(num1, num2, operation)
print(f"Результат: {result}")
