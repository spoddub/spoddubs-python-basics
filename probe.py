s = input()
numbers = s.split()
new_numbers = []
for i in numbers:
    x = int(i) ** 3
    new_numbers.append(x)
print(*new_numbers)

















