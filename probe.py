a, b = 1, 10
total = 0
for _ in range(a, b + 1):
    if _ ** 3 % 10 == 4 or _ ** 3 % 10 == 9:
        total = total + 1
print(total)

