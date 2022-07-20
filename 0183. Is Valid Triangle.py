# Напишите функцию is_valid_triangle(side1, side2, side3),
# которая принимает в качестве аргументов три натуральных числа,
# и возвращает значение True если существует невырожденный треугольник со сторонами side1, side2, side3
# и False в противном случае.
#
# Примечание. Следующий программный код:
#
# print(is_valid_triangle(2, 2, 2))
# print(is_valid_triangle(2, 3, 10))
# print(is_valid_triangle(3, 4, 5))
# должен выводить:
#
# True
# False
# True

def is_valid_triangle(side1, side2, side3):
    if side1 + side2 > side3 and side2 + side3 > side1 and side1 + side3 > side2:
        return True
    else:
        return False

a, b, c = int(input()), int(input()), int(input())

print(is_valid_triangle(a, b, c))