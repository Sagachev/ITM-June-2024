import math
# 1.	Дана сторона квадрата a. Найти его периметр P = 4•a
a = int(input())
p = a * 4
print(p)


# 2.	Дана сторона квадрата a. Найти его площадь{{ S = a2}}
a = int(input())
s = a ** 2
print(s)

# 3.	Даны стороны прямоугольника a и b. Найти его площадь S = a•b и периметр P = 2•(a + b)
a,b =int(input()), int(input())
s = a * b
p = 2 * (a + b)
print(s, p, sep='\n')

# 4.	Дан диаметр окружности d. Найти ее длину{{ L = π•d, π = 3.14}}
d = int(input())
l = 3.14 * d
print(l)

# # 5.	Дана длина ребра куба a. Найти объем куба V = a3 и площадь его поверхности S = 6•a2
a = int(input())
v = a ** 3
s = 6 * (a ** 2)
print(v,s, sep='\n')
# 6.	Даны длины ребер a, b, c прямоугольного параллелепипеда. Найти его объем V = a•b•c и площадь поверхности S = 2•(a•b + b•c + a•c)
a,b,c = int(input()), int(input()), int(input())
v = a * b * c
s = 2 * (a * b + b * c + a * c)
print(v, s, sep='\n')
# 7.	Найти длину окружности L и площадь круга S заданного радиуса R: L = 2•π•R, S = π•R2, π=3.14
r = int(input())
l = 2 * 3.14 * r
s = 3.14 * r ** 2
print(l, s, sep='\n')
# 8.	Даны два числа a и b. Найти их среднее арифметическое: (a + b)/2
a,b = int(input()), int(input())
num = (a + b) / 2
print(num)

# 9.	Даны два неотрицательных числа a и b. Найти их среднее геометрическое, т. е. квадратный корень из их произведения: (a•b)1/2
a,b = int(input()), int(input())
num = a * b
sqrt = math.sqrt(num)
print(sqrt)

# 10.	Даны два ненулевых числа. Найти сумму, разность, произведение и частное их квадратов.
a,b = int(input()), int(input())
a = a ** 2
b = b ** 2
sum = a + b
dif1 = a - b
dif2 = b - a
mul = a * b
num = a / b
print(sum, dif1, dif2, mul, num, sep='\n')

