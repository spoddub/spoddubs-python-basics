def is_password_good(password):
    if len(password) < 8:
        return False
    digit_flag = False
    upper_flag = False
    lower_flag = False
    for i in password:
        if i.isdigit():
            digit_flag = True
        elif i.isupper():
            upper_flag = True
        elif i.islower():
            lower_flag = True
    return digit_flag and upper_flag and lower_flag

# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))