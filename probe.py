n = int(input())
my_list = []
for _ in range(n):
    m = int(input())
    my_list.append(m)
my_list.remove(min(my_list))
my_list.remove(max(my_list))
print(*my_list, sep='\n')




















