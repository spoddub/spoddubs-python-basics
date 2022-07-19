def print_digit_sum(n):
    c = 0
    while n != 0:
        b = n % 10
        c += b
        n = n // 10
    print(c)
n = int(input())
print_digit_sum(n)











