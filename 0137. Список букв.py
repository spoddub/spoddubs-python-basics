# На вход программе подается одно число n.
# Напишите программу, которая выводит список,
# состоящий из n букв английского алфавита ['a', 'b', 'c', ...] в нижнем регистре.
# Формат входных данных
# На вход программе подается натуральное число n.
# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.
n = int(input())
s = ''
for i in range(n):
    s += chr(97 + i)
print(list(s))