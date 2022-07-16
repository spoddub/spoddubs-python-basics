# Джим Хоппер с помощью радиоприемника пытается получить сообщение Оди.
# На приемник ему поступает n различных последовательностей кода Морзе.
# Декодировав их, он получает последовательности из цифр и строчного латинского алфавита,
# при этом во всех сообщениях Оди содержится число 11, причем минимум 3 раза.
# Помогите определить Джиму количество сообщений от Оди.
# Формат входных данных
# В первой строке подаётся число n – количество сообщений,
# в последующих n строках вводятся строки, содержащие латинские строчные буквы и цифры.
# Формат выходных данных
# Программа должна вывести количество строк в которых содержится число 11 минимум 3 раза.
n = int(input())
total = 0
for _ in range(n):
    s = input()
    if s.count('11') >= 3:
        total += 1
print(total)