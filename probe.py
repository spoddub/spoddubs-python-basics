n = int(input())
s = input()
for i in range(len(s)):
    f = s[i]
    a = ord(s[i]) + (26 - n)
    if 97 <= a <= 122:
        print(chr(a), end='')
        continue
    if a > 122:
        print(chr(96 + (a - 122)), end='')
        continue







