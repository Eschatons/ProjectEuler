# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 12:19:53 2016

@author: efron
"""

# project euler question 038
from primes import sieve as primes_under
from typing import Callable, List
from collections import defaultdict


"""
The number 3797 has an interesting property. Being prime itself, 
it is possible to continuously remove digits from left to right, 
and remain prime at each stage: 3797, 797, 97, and 7. Similarly we
 can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable
 from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered 
to be truncatable primes.
"""

# we use dynamic programming and closures
# 0: find primes
# 1: maintain dict of leftTruncatable and rightTruncatable primes
# 2a: check rightcut prime against rightTruncatable
# 2b: check leftcut prime against leftTruncatable 

def find_truncatable_primes_under(n: int) -> List[int]:
    def create_is_truncatable() -> Callable:
        leftTrunc = defaultdict(bool)
        rightTrunc = defaultdict(bool)
        for x in ('2', '3', '5', '7'):
            leftTrunc[x] = True
            rightTrunc[x] = True         
            
        def is_truncatable(n: str) -> bool:
            nonlocal leftTrunc, rightTrunc
            left, right = n[1:], n[:-1]
            if leftTrunc[left]:
                leftTrunc[n] = True
            if rightTrunc[right]:
                rightTrunc[n] = True
            return leftTrunc[n] and rightTrunc[n]
            
        return is_truncatable
    
    primes = (str(x) for x in primes_under(n) if x > 9)
    is_truncatable = create_is_truncatable()
    
    truncPrimes = []
    for prime in primes:
        if is_truncatable(prime):
            truncPrimes.append(int(prime))
    return truncPrimes
    
    
truncatablePrimes = find_truncatable_primes_under(10**7)
print(truncatablePrimes)
print(sum(truncatablePrimes))