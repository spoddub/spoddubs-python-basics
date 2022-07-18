n = int(input())
Negatives = []
Zeros = []
Positives = []
for _ in range(n):
    m = int(input())
    if m > 0:
        Positives.append(m)
    elif m == 0:
        Zeros.append(m)
    else:
        Negatives.append(m)
print(*Negatives, sep='\n')
print(*Zeros, sep='\n')
print(*Positives, sep='\n')





















