n = int(input())
my_list = []
for _ in range(n):
    m = input()
    if m not in my_list:
        my_list.append(m)
    else:
        continue
print(*my_list, sep='\n')


















