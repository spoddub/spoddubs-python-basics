# На вход программе подается строка текста, содержащая имя, отчество и фамилию человека.
# Напишите программу, которая выводит инициалы человека.
# Формат входных данных
# На вход программе подается строка текста, содержащая имя, отчество и фамилию человека.
# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.
s = input()
words = s.split()
new_words = []
for i in words:
    new_words.append(i[0])
print(*new_words, sep='.', end='.')

