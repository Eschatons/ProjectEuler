# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 19:04:14 2016

@author: efron
"""

# euler 070
"""
Euler's Totient function, φ(n) [sometimes called the phi function], is used to
determine the number of positive numbers less than or equal to n which are 
relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all 
less than nine and relatively prime to nine, φ(9)=6.

The number 1 is considered to be relatively prime to every positive number, 
so φ(1)=1.

Interestingly, φ(87109)=79180, and it can be seen that 87109 is a permutation 
of 79180.

Find the value of n, 1 < n < 10**7, for which φ(n) is a permutation of n
and the ratio n/φ(n) produces a minimum.
"""


from collections import namedtuple
from primes import sieve
from itertools import combinations
from math import sqrt
elem = namedtuple('elem', ['n', 'φ', 'ratio', 'primeDivisors'])

# the fewer the prime divisors, the higher the ratio n/φ(n).
# since if p a prime it's totient is p-1, we can't have just one prime divisor
# so we try two.

# we think that two primes around sqrt(10**7) will give the best result
# but we give a little more breathing room

primes = sieve(int(10*sqrt(10**7)))
totients = []
for a, b in combinations(primes, 2):
    n = a*b
    if n < 10**7:
        totient = (a-1)*(b-1)
        if sorted(str(totient)) == sorted(str(n)) and n < 10**7:
            totients.append(elem(n, totient, n/totient, (a, b)))
totients.sort(key = lambda x: x.ratio)

for x in range(5):
    print(totients[x])
""" first attempt ('brute force') is preserved below: it gave me the idea 
but ran too slow """
#from factor import FactorizationDict
#F = FactorizationDict(maxElem = 10**5, fillFactorTree=True)
#
#totientPermutations = {}
#def totientIsPermutation(x: int, totient: int) -> bool:
#    if sorted(str(x)) == sorted(str(totient)):
#        return True
#    else:
#        return False
#
#totients = []
#for x in F:
#    totient = F.totient(x)
#    if totientIsPermutation(x, totient):
#        primeDivisors = tuple(x for x in F[x])
#        totients.append(elem(x, totient, x/totient, primeDivisors))
#
#totients = sorted(totients, key = lambda x: x.ratio)
#for totient in totients:
#    print(totient)
    