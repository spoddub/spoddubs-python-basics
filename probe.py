n = int(input())
my_list = []
for _ in range(n):
    m = int(input())
    my_list.append(m)
print(*my_list, sep='\n')
print()
new_list = []
for num in my_list:
    number = num ** 2 + num * 2 + 1
    new_list.append(number)
print(*new_list, sep='\n')


















