# На вход программе подается натуральное число n, а затем n целых чисел.
# Напишите программу, которая создает из указанных чисел список их кубов.
# Формат входных данных
# На вход программе подаются натуральное число nnn, а затем nnn целых чисел, каждое на отдельной строке.
# Формат выходных данных
# Программа должна вывести список, состоящий из кубов указанных чисел.
n = int(input())
my_list = []
for i in range(n):
    m = int(input())
    my_list.append(m ** 3)
print(my_list)