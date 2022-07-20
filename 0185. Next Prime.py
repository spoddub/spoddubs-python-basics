# Напишите функцию get_next_prime(num), которая принимает в качестве аргумента натуральное число num
# и возвращает первое простое число большее числа num.
#
#  Примечание. Следующий программный код:
#
# print(get_next_prime(6))
# print(get_next_prime(7))
# print(get_next_prime(14))
# должен выводить:
#
# 7
# 11
# 17

def get_next_prime(num):
    num += 1
    for i in range(2, num):
        if num % i == 0:
            return get_next_prime(num)
    return num

n = int(input())

print(get_next_prime(n))