# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 17:35:46 2016

@author: efron
"""
"""
We shall say that an n-digit number is pandigital 
if it makes use of all the digits 1 to n exactly once.
 For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists? """

# let's examine bounds. our largest possible pandigital is
# 987654321
# there are this many pandigitals:
# 9! + 8! + 7! + 6! + 5! + 4! + 3! + 2! + 1!

from itertools import permutations
from primes import is_prime

def gen_pandigitals():
    """ generate pandigitals, starting with the largest """
    digits = '123456789'
    for i in range(10, 1, -1):
        for x in permutations(reversed(digits[:i])):
            yield(int(''.join(x)))
            
pandigitals = gen_pandigitals()
def largest_pandigital_prime():
    for n in pandigitals:
        if is_prime(n):
            return n

print(largest_pandigital_prime())