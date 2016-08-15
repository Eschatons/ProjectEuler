# -*- coding: utf-8 -*-
"""

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n 
exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, 
multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written 
as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include
it once in your sum.
"""

def unique_chars(x):
    return set(str(x))

from itertools import chain
trueRange = list(chain([range(10),
            (x for x in range(10, 100) if len(unique_chars(x)) == 2),
            (x for x in range(100, 1000) if len(unique_chars(x)) == 3),
            (x for x in range(1000, 10000) if len(unique_chars(x)) == 4)]
            ))

def chars_overlap(a, b):
    if unique_chars(a) - unique_chars(b):
        return True
    else:
        return False

products = set()        
for a in trueRange:
    for b in trueRange:
        if not chars_overlap(a, b):
            c = a*b
            concatanation = str(a)+str(b)+str(c)
            if sorted(concatanation) == sorted('0123456789'):
                products |= {c}