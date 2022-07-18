n = int(input())
my_list = []
for _ in range(n):
    stroka = input()
    my_list.append(stroka)
k = input()
for searchies in my_list:
    if k in searchies or k.title() in searchies or k.swapcase() in searchies:
        print(searchies)
















