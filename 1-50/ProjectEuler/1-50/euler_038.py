# -*- coding: utf-8 -*-


""" euler 38: pandigital multiples """
for n in reversed(range(333)):
    numbers = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
    if set(str(n) + str(n * 2) + str(n * 3)) == numbers:
        number = n
        break
print(int(str(number) + str(number * 2) + str(3 * number)))

ans = 327654981
