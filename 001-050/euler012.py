# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 09:57:54 2016

@author: efron
"""

from factor import FactorizationDict
F = FactorizationDict(maxElem = 10**8)

def triangular(n: int) -> int:
    return (n*(n+1))//2

def find_first_triangular_with_500_divisors():
    n = 1
    divisors = 1
    maxSoFar = 1
    while divisors < 500:
        n += 1
        divisors = F.count_divisors(triangular(n))
        if divisors > maxSoFar:
            maxSoFar = divisors
            print(maxSoFar)
    return n
    
n = find_first_triangular_with_500_divisors()