# 1.	Дано целое число A. Проверить истинность высказывания: «Число A является положительным».
a = int(input())
if a >= 0:
    print(True)
else:
    print(False)

# 2.	Дано целое число A. Проверить истинность высказывания: «Число A является нечетным».
a = int(input())
if a % 2 != 0:
    print(True)
else:
    print(False)

# 3.	Дано целое число A. Проверить истинность высказывания: «Число A является четным».
a = int(input())
if a % 2 == 0:
    print(True)
else:
    print(False)

# 4.	Даны два целых числа: A, B. Проверить истинность высказывания: «Справедливы неравенства A > 2 и B ≤ 3».
a,b = int(input()), int(input())
if a > 2 or b <= 3:
     print(True)
else:
     print(False)

# 5.	Даны два целых числа: A, B. Проверить истинность высказывания: «Справедливы неравенства A ≥ 0 или B < −2».
a,b = int(input()), int(input())
if a > 2 or b <= 3:
     print(True)
else:
     print(False)

# 6.	Даны три целых числа: A, B, C. Проверить истинность высказывания: «Справедливо двойное неравенство A < B < C».
a,b,c = int(input()), int(input()), int(input())
if a < b < c:
     print(True)
else:
     print(False)

# 7.	Даны три целых числа: A, B, C. Проверить истинность высказывания: «Число B находится между числами A и C».
a,b,c = int(input()), int(input()), int(input())
if a < b < c or c < b < a:
     print(True)
else:
     print(False)

# 8.	Даны два целых числа: A, B. Проверить истинность высказывания: «Каждое из чисел A и B нечетное».
a,b = int(input()), int(input())
if a % 2 != 0 and b % 2 != 0:
     print(True)
else:
     print(False)

# 9.	Даны два целых числа: A, B. Проверить истинность высказывания: «Хотя бы одно из чисел A и B нечетное».
a,b = int(input()), int(input())
if a % 2 != 0 or b % 2 != 0:
     print(True)
else:
     print(False)

# 10.	Даны два целых числа: A, B. Проверить истинность высказывания: «Ровно одно из чисел A и B нечетное»
a,b = int(input()), int(input())
if a % 2 != 0 and b % 2 == 0 or a % 2 == 0 and b % 2 != 0:
     print(True)
else:
     print(False)