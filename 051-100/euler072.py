# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 09:49:45 2016

@author: efron
"""
#euler072
"""
Consider the fraction, n/d, where n and d are positive integers.
If n<d and HCF(n,d)=1, it is called a reduced proper fraction.
If we list the set of reduced proper fractions for d ≤ 8 in 
ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2,
4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 21 elements in this set.
How many elements would be contained in the set of reduced proper fractions
for d ≤ 1,000,000?
"""

# we note without proof the isomorphism between the sets of reduced proper
# fractions of n and the multiplicative groups modulo n.
# since |Z(n)|= φ(n), we count sum(φ(d) for d in range(10**6))

from factor import FactorizationDict

F = FactorizationDict(10**6+1, fillFactorTree=True)
φ = F.totient
print('the # of reduced proper fractions for d <= 8 is:')
example = sum(φ(n) for n in range(2, 9))
print(example)
print('the # of reduced proper fractions for d <= 10**6 is:')
answer = sum(φ(n) for n in range(2, 10**6+1))
print(answer) 