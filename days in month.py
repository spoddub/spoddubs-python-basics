# my first kinda program on python
# lets tell user how many days in month of their choice
user_input = input("please enter month number: ")
month = int(user_input)
if month == 1:
    print('31')
elif month == 3:
    print(31)
elif month == 5:
    print(31)
elif month == 7:
    print(31)
elif month == 8:
    print(31)
elif month == 10:
    print(31)
elif month == 12:
    print(31)
elif month == 2:
    print(28)
else:
    print(30)

print('you entered', month)
