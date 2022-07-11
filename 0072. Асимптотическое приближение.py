# На вход программе подается натуральное число n.
# Напишите программу, которая вычисляет значение асимптотическоого приближения
from math import *
counter = 0
n = int(input())
for i in range(1, n+1):
    counter +=  1 / i
print(counter - log(n))

