# Напишите программу, в которой рассчитывается сумма и произведение цифр положительного трёхзначного числа.
# Формат входных данных
# На вход программе подаётся положительное трёхзначное число.
# Формат выходных данных
# Программа должна вывести два числа с поясняющим текстом: сумма цифр и произведение цифр.
num = int(input())
last = num % 10
middle = (num % 100) // 10
first = num // 100
summ = int(last + middle + first)
proizv = int(last * middle * first)
print('Сумма цифр =', summ)
print('Произведение цифр =', proizv)