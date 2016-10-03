# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 12:56:07 2016

@author: efron
"""
"""
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
"""
def product(iterable):
    total = 1
    for x in iterable:
        total *= x
    return total

def gen_digits():
    n = 0
    while True:
        n += 1
        for digit in str(n):
            yield int(digit)
    
item = (10**n for n in range(7))
digits = gen_digits()
held = []
currentItem = next(item)
for k in range(1, 10**6):
    currentDigit = next(digits)
    if k == currentItem:
        held.append(currentDigit)
        currentItem = next(item)


answer = product(held)

print(answer)