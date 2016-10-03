# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 09:03:10 2016

@author: efron
"""

# euler 050
"""
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime 
below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, 
contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most 
consecutive primes?
"""
from primes import sieve
import numpy as np

consecutiveSumPrimes = {}
primes = np.array(sieve(10**6//2), dtype = 'uint64')
primeSet = set(sieve(10**6))
shift = 0
primeSums = primes
while len(primeSums) > 0:
    shift += 1
    primeSums = primeSums[1:] + primes[:-shift]
    sumPrimes = [x for x in primeSums if x in primeSet]
    if len(sumPrimes) > 0:
        print(sumPrimes)
        consecutiveSumPrimes[shift+1] = sumPrimes