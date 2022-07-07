# Напишите программу, которая определяет наименьшее из четырёх чисел.

# Формат входных данных
# На вход программе подаётся четыре целых числа.

# Формат выходных данных
# Программа должна вывести наименьшее из четырёх чисел.
n, n2, n3, n4 = int(input()), int(input()), int(input()), int(input())
if n < n2:
    minimum = n
else:
    minimum = n2
if n3 < n4:
    minimum2 = n3
else:
    minimum2 = n4
if minimum < minimum2:
    print(minimum)
else:
    print(minimum2)