# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 15:09:37 2016

@author: efron
"""

"""Let d(n) be defined as the sum of proper divisors of n (numbers less than n
which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and
each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 
and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 
and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000."""

from itertools import combinations
from factor import FactorizationDict

def product(iterable):
    total = 1
    for item in iterable:
        total *= item
    return total
    
def divisors_from_factorization(factors):
    explodedFactors = []
    for factor in factors:
        power = factors[factor]
        explodedFactors.extend([factor]*power)
    
    def nontrivial_factor_combinations(iterable):
        for n in range(1, len(iterable)):
            combo = combinations(iterable, n)
            for elem in combo:
                yield elem
                
    
    divisors = {product(n) for n in nontrivial_factor_combinations(explodedFactors)}
    divisors |= {1}
    return list(divisors)

def find_amicable_numbers():
    
    factors = FactorizationDict(maxElem = 2*10**5, fillFactorTree=True)
    properDivisorSum = {}
    amicableNumbers = []
    for a in range(1, 10000):
        b = sum(divisors_from_factorization(factors[a]))
        properDivisorSum[a] = b
        properDivisorSum[b] = sum(divisors_from_factorization(factors[b]))
        if properDivisorSum[b] == a and b != a:
            amicableNumbers.append(a)
    return amicableNumbers

amicable = find_amicable_numbers()
print(amicable)
print(sum(amicable))