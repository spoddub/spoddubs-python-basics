# Напишите программу, которая определяет, являются ли три заданных числа (в указанном порядке) последовательными членами арифметической прогрессии.

# Формат входных данных
# На вход программе подаются три числа, каждое на отдельной строке.

# Формат выходных данных
# Программа должна вывести «YES» или «NO» (без кавычек) в соответствии с условием задачи.
n, n1, n2 = int(input()), int(input()), int(input())
if n1 - n == n2 - n1:
    print('YES')
else:
    print('NO')