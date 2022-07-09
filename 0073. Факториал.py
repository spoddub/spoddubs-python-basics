# На вход программе подается натуральное число n.
# Напишите программу, которая вычисляет n!.
n = int(input())
total = 1
for i in range(1, n + 1):
    total *= i
print(total)