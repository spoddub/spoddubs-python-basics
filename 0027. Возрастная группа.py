# Hапишите программу, которая по введённому возрасту пользователя сообщает, к какой возрастной группе он относится:

# до 13 включительно – детство;
# от 14 до 24 – молодость;
# от 25 до 59 – зрелость;
# от 60 – старость.

# Формат входных данных
# На вход программе подаётся одно целое число – возраст пользователя.

# Формат выходных данных
# Программа должна вывести название возрастной группы.
age = int(input())
if age <= 13:
    print('детство')
if age >= 14 and age <= 24:
    print('молодость')
if age >= 25 and age <= 59:
    print('зрелость')
if age >= 60:
    print('старость')