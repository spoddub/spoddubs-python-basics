# Вводятся 3 строки в случайном порядке.
# Напишите программу, которая выясняет можно ли из длин этих строк построить возрастающую арифметическую прогрессию.
# Формат входных данных
# На вход программе подаются три строки, каждая на отдельной строке.
# Формат выходных данных
# Программа должна вывести строку «YES», если из длин введенных слов можно построить арифметическую прогрессию, «NO» в ином случае.
a, b, c = len(input()), len(input()), len(input())
maximum = 0
minimum = 0
middle = 0
if a < b and a < c:
    minimum = a
elif b < a and b < c:
    minimum = b
elif c < a and c < b:
    minimum = c
if a > b and a > c:
    maximum = a
elif b > a and b > c:
    maximum = b
elif c > a and c > b:
    maximum = c
if b < a < c or c < a < b:
    middle = a
elif a < b < c or c < b < a:
    middle = b
elif a < c < b or b < c < a:
    middle = c
first = maximum - middle
last = middle - minimum
if first == last:
    print('YES')
else:
    print('NO')
