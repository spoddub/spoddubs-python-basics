# Даны три вещественных числа a , b, c. Напишите программу, которая находит вещественные корни квадратного уравнения
# Формат входных данных
# На вход программе подается три вещественных числа a , b, c каждое на отдельной строке.
# Формат выходных данных
# Программа должна вывести вещественные корни уравнения если они существуют или текст «Нет корней» в противном случае.
# Примечание. Если уравнение имеет два корня, то следует вывести их в порядке возрастания.
import math
from math import *
a, b, c = float(input()), float(input()), float(input())
d = (b ** 2) - (4 * (a * c))
x1, x2 = 0, 0
if  d > 0:
    x1 = ((-b + sqrt(d)) / (2 * a))
    x2 = ((-b - sqrt(d)) / (2 * a))
    print(min(x1, x2))
    print(max(x1, x2))
elif d == 0:
    print(-b / (2 * a))
else:
    print('Нет корней')