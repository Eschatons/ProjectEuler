# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 15:15:30 2016

@author: efron
"""
"""
The proper divisors of a number are all the divisors excluding the number 
itself. For example, the proper divisors of 28 are 1, 2, 4, 7, and 14. 
As the sum of these divisors is equal to 28, we call it a perfect number.

Interestingly the sum of the proper divisors of 220 is 284 and the sum 
of the proper divisors of 284 is 220, forming a chain of two numbers. 
For this reason, 220 and 284 are called an amicable pair.

Perhaps less well known are longer chains. For example, starting with 
12496, we form a chain of five numbers:

12496 → 14288 → 15472 → 14536 → 14264 (→ 12496 → ...)

Since this chain returns to its starting point, it is called an 
amicable chain.

Find the smallest member of the longest amicable chain 
with no element exceeding one million.
"""

from factor import FactorizationDict
F = FactorizationDict(maxElem = 10**6+1, fillFactorTree=True)

def divisor_sum(n):
    return sum(F.divisors(n))
def is_amicable_chain_factory():
    goodChains = dict()
    badChains = set()
    def is_amicable_chain(n):
        nonlocal goodChains, badChains
        if n in goodChains:
            return True, goodChains[n]
        if n in badChains:
            return False, None

        seen = set()
        chain = []
        someGoodChain = False
        while n <= 10**6:

            chain.append(n)
            seen |= n
            n = divisor_sum(n)

            if n in seen:
                someGoodChain = True
                index = chain.index(n)
                someGoodChain = True
                goodChain = chain[index:]
                badChain = chain[:index]
                break
        if someGoodChain:
            for elem in goodChain:
                goodChains[elem] = goodChain
                badChains |= set(badChain)
        badChain = chain
        badChains |= set(badChain)
z        return False, None
is_amicable_chain = is_amicable_chain_factory()
for n in range(10**3):
    success, result = is_amicable_chain(n)
    if success:
        print(result)

            