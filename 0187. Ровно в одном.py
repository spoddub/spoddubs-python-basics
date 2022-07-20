# Напишите функцию is_one_away(word1, word2),
# которая принимает в качестве аргументов два слова word1 и word2 и возвращает значение True
# если слова имеют одинаковую длину и отличаются ровно в 1 символе и False в противном случае.
#
#  Примечание. Следующий программный код:
#
# print(is_one_away('bike', 'hike'))
# print(is_one_away('water', 'wafer'))
# print(is_one_away('abcd', 'abpo'))
# print(is_one_away('abcd', 'abcde'))
# должен выводить:
#
# True
# True
# False
# False

# объявление функции
def is_one_away(word1, word2):
    if len(word1) == len(word2):
        counter = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                counter += 1
        if counter == 0 or counter >= 2:
            return False
        else:
            return True
    else:
        return False




# считываем данные
txt1 = input()
txt2 = input()

# вызываем функцию
print(is_one_away(txt1, txt2))