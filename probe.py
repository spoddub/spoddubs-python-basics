def is_prime(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    else:
        return True

# считываем данные
n = int(input())

# вызываем функцию
print(is_prime(n))