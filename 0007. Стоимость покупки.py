# Напишите программу, которая считает стоимость трех компьютеров, состоящих из монитора, системного блока, клавиатуры и мыши.

# Формат входных данных
# На вход программе подаётся четыре целых числа, каждое на отдельной строке. В первой строке — стоимость монитора, во второй строке — стоимость системного блока, в третьей строке — стоимость клавиатуры и в четвертой строке — стоимость мыши.

# Формат выходных данных
# Программа должна вывести одно число – стоимость покупки (трех компьютеров).
monitor = int(input())
system_block = int(input())
keyboard = int(input())
mouse = int(input())
money = int((monitor + system_block + keybord + mouse) * 3) 
print(money)