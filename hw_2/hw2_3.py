#Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

n = int(input('введите число: '))
a = 2
i = 0
while a ** i < n:
    print(a ** i, end = (' '))
    i += 1
