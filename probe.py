def find_all(target, symbol):
    li = []
    for i in range(len(target)):
        if target[i] == symbol:
            li.append(i)
    return li

s = input()
char = input()

print(find_all(s, char))








