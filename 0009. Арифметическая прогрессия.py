# Арифметической прогрессией называется последовательность чисел a1,a2,...,an a_1, a_2, ..., a_n a1​,a2​,...,an​, каждое из которых, начиная с a2 a_2 a2​, получается из предыдущего прибавлением к нему одного и того же постоянного числа d d d (разность прогрессии)
# Входные данные
# На вход программе подаётся три целых числа: a1 a_1 a1​, d d d и n n n, каждое на отдельной строке.

# Выходные данные
# Программа должна вывести n n n-ый член арифметической прогрессии.
a_1, d, n = int(input()), int(input()), int(input())
an = int(a_1 + (d * (n - 1)))
print(an)