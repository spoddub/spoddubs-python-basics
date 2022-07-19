def get_factors(num):
    my_list = []
    for i in range(1, num + 1):
        if num % i == 0:
            my_list.append(i)
    return len(my_list)


n = int(input())

print(get_factors(n))









