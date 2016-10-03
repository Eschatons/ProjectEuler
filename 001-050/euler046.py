# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 11:16:37 2016

@author: efron
"""

"""
It was proposed by Christian Goldbach that every odd composite number can be 
written as the sum of a prime and twice a square.

9 = 7 + 2×1**2
15 = 7 + 2×2**2
21 = 3 + 2×3**2
25 = 7 + 2×3**2
27 = 19 + 2×2**2
33 = 31 + 2×1**2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a 
prime and twice a square?
"""

from primes import sieve

primes = set(sieve(10**5))

primeCompositeSums = {prime+(2*(n**2)) for n in range(10**3) for prime in primes}

oddComposites = (x for x in range(2, 10**5) if x not in primes and x % 2)

for x in oddComposites:
    if x not in primeCompositeSums:
        print(x)
        break