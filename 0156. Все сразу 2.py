# Дополните приведенный код, чтобы он:
# Заменил второй элемент списка на 17;
# Добавил числа 4, 5 и 6 в конец списка;
# Удалил первый элемент списка;
# Удвоил список;
# Вставил число 25 по индексу 3;
# Вывел список, с помощью функции print()
numbers = [8, 9, 10, 11]
numbers.remove(numbers[1])
numbers.insert(1, int(17))
numbers.append(int(4))
numbers.append(int(5))
numbers.append(int(6))
numbers.remove(numbers[0])
numbers *= 2
numbers.insert(3, int(25))
print(numbers)