# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 11:00:51 2016

@author: efron
"""
"""
We shall say that an n-digit number is pandigital if it makes use of all the 
digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, 
containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity
can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only 
include it once in your sum.
"""
from itertools import combinations

def is_pandigital(n):
    if sorted(str(n)) == list('123456789'):
        return True
    return False
# let's look at some bounds. given a*b = c, we note that
# digits(c) >= max(digits a, digits b)

# so then we can have at most 4 digits in a or b.


digits = '123456789'
pandigitals = set()
for a in range(10**4):
    for b in range(10**4):
        c = a*b
        concat = str(a)+str(b)+str(c)
        if is_pandigital(concat):
            a, b = max(a, b), min(a, b)
            print('{0}*{1}={2}'.format(a, b, c))
            pandigitals |= {c}
        if len(concat) > 9:
            break

pandigitals = sorted(pandigitals)
print(pandigitals)
print(sum(pandigitals))