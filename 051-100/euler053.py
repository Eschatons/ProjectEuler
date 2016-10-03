# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 09:28:07 2016

@author: efron
"""

# euler053
'''
There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, 5C3 = 10.

In general,

nCr =	
n! / (r! (n−r)!)
,where r ≤ n, n! = n×(n−1)×...×3×2×1, and 0! = 1.
It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.

How many, not necessarily distinct, values of  nCr, for 1 ≤ n ≤ 100, 
are greater than one-million?
'''

from math import factorial
def nchoosek(n: int, k: int) -> int:
    def partial_factorial(n: int, k: int) -> int:
        # returns n! / k!
        total = 1
        for j in range(n, k, -1):
            total *= j
        return total
    
    if n < 1 or k < 1:
        raise(ValueError('n choose k defined only for n >= k > 0'))
    
    k = max(k, n-k)
    return int(round(partial_factorial(n, n-k) / factorial(k)))
    
    

def count_large_n_choose_k(threshold = 10**6):
    overThreshold = 0
    for n in range(1, 101):
        for k in range(1, n+1):
            if nchoosek(n, k) > threshold:
                overThreshold += 1
    return overThreshold

overThreshold = count_large_n_choose_k()

print(overThreshold)