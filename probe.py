def get_days(month):
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        return 31
    if month == 2:
        return 28
    else:
        return 30

num = int(input())
print(get_days(num))










