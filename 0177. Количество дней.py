# Напишите функцию get_days(month), которая принимает в качестве аргумента номер месяца
# и возвращает количество дней в данном месяце.
# Примечание 1. Гарантируется, что передаваемый аргумент находится в диапазоне от 1 до 12.
# Примечание 2. Считайте, что год является невисокосным.
# Примечание 3. Следующий программный код
# print(get_days(1))
# print(get_days(2))
# print(get_days(9))
# должен выводить:
# 31
# 28
# 30
def get_days(month):
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        return 31
    if month == 2:
        return 28
    else:
        return 30

num = int(input())
print(get_days(num))