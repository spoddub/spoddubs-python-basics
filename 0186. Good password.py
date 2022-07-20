# возвращает значение True если пароль является надежным и False в противном случае.
#
# Пароль является надежным если:
#
# его длина не менее 8 символов;
# он содержит как минимум одну заглавную букву (верхний регистр);
# он содержит как минимум одну строчную букву (нижний регистр);
# он содержит хотя бы одну цифру.
#
#  Примечание. Следующий программный код:
#
# print(is_password_good('aabbCC11OP'))
# print(is_password_good('abC1pu'))
# должен выводить:
#
# True
# False

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