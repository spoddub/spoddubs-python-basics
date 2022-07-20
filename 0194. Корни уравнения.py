# Напишите функцию solve(a, b, c), которая принимает в качестве аргументов три целых числа a, b, c –
# коэффициенты квадратного уравнения x^2 + bx + c = 0 и возвращает его корни в порядке возрастания.

from math import sqrt

# объявление функции
def solve(a, b, c):
    d = (b ** 2) - (4 * (a * c))
    x1, x2 = 0, 0
    if d > 0:
        x1 = ((-b + sqrt(d)) / (2 * a))
        x2 = ((-b - sqrt(d)) / (2 * a))
        return min(x1, x2), max(x1, x2)
    elif d == 0:
        return -b / (2 * a)

# считываем данные
a, b, c = int(input()), int(input()), int(input())

# вызываем функцию
x1, x2 = solve(a, b, c)
print(x1, x2)