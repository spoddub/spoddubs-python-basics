num = int(input())
for i in range(num):
    for j in range(min(i + 1, num - i)):
        print('*', end='')
    print()