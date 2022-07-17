s = input()
count = 0
letter = 0
for i in s:
    if s.count(i) >= count:
        count = s.count(i)
        letter = i
print(i)



