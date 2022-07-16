s = input()
total = 0
for i in s:
    if s[i] != s.title():
        total += 1
print(total)