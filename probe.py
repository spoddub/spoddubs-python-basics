n = int(input())
my_list = []
for _ in range(n):
    m = input()
    my_list.append(m)
k = int(input())
new_list = []
for i in range(k):
    stroka = input().lower()
    if stroka in my_list.lower:
        new_list.append(stroka)
    





















