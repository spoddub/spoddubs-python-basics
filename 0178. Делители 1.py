# Напишите функцию get_factors(num), принимающую в качестве аргумента натуральное число
# и возвращающую список всех делителей данного числа.
# Примечание. Следующий программный код:
# print(get_factors(1))
# print(get_factors(5))
# print(get_factors(10))
# должен выводить:
# [1]
# [1, 5]
# [1, 2, 5, 10]
def get_factors(num):
    my_list = []
    for i in range(1, num + 1):
        if num % i == 0:
            my_list.append(i)
    return my_list

n = int(input())

print(get_factors(n))