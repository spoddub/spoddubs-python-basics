# Напишите программу определяющую площадь круга и длину окружности по заданному радиусу R.
#
# Формат входных данных
# На вход программе подается одно вещественное число R​.
#
# Формат выходных данных
# Программа должна вывести два числа – площадь круга и длину окружности радиуса R.
from math import *
r = float(input())
s = pi * r ** 2
c = 2 * pi * r
print(s)
print(c)