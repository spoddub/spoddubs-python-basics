def quick_merge(lst1, lst2):
    res = []
    p1, p2 = 0, 0
    while p1 < len(lst1) and p2 < len(lst2):
        if lst1[p1] < lst2[p2]:
            res.append(lst1[p1])
            p1 += 1
        else:
            res.append(lst2[p2])
            p2 += 1
    if p1 == len(lst1):
        res += lst2[p2:]
    else:
        res += lst1[p1:]
    return res


res = []
for _ in range(int(input())):
    num = [int(c) for c in input().split()]
    res = quick_merge(res, num)
print(*res)







