# Напишите функцию convert_to_python_case(text), которая принимает в качестве аргумента строку в
# «верблюжьем регистре» и преобразует его в «змеиный регистр».
#
# Примечание 1. Почитать подробнее о стилях именования можно тут.
#
# Примечание 2. Следующий программный код:
#
# print(convert_to_python_case('ThisIsCamelCased'))
# print(convert_to_python_case('IsPrimeNumber'))
# должен выводить:
#
# this_is_camel_cased
# is_prime_number

# объявление функции
def convert_to_python_case(text):
    for i in text:
        if i in 'QWERTYUIOPASDFGHJKLZXCVBNM':
            text = text.replace(i, '_' + i.lower())
    return text[1:]

# считываем данные
txt = input()

# вызываем функцию
print(convert_to_python_case(txt))