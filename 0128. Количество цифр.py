# На вход программе подается строка текста.
# Напишите программу, которая подсчитывает количество цифр в данной строке.
# Формат входных данных
# На вход программе подается строка текста.
# Формат выходных данных
# Программа должна вывести количество цифр в данной строке.
k = 0
for c in input():
    if '0'<= c <='9':
        k += 1
print(k)

