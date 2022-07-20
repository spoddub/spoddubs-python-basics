# Напишите функцию get_circle(radius), которая принимает в качестве аргумента радиус окружности
# и возвращает два значения: длину окружности и площадь круга, ограниченного данной окружностью.
# Для числа π используйте глобальную константу из модуля math.

from math import pi


def get_circle(radius):
    c = 2 * (pi * radius)
    s = pi * radius ** 2
    return c, s


# считываем данные
r = float(input())

# вызываем функцию
length, square = get_circle(r)
print(length, square)