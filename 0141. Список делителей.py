# На вход программе подается натуральное число n.
# Напишите программу, которая создает список состоящий из делителей введенного числа.
# Формат входных данных
# На вход программе подается натуральное число nnn.
# Формат выходных данных
# Программа должна вывести список, состоящий из делителей введенного числа.
n = int(input())
my_list = []
for i in range(1, n + 1):
    if n % i == 0:
        my_list.append(i)
print(my_list)