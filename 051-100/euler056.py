# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 11:47:30 2016

@author: efron
"""

"""A googol (10**100) is a massive number: one followed by one-hundred zeros;
 100**100 is almost unimaginably large: one followed by two-hundred zeros. 
 Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, ab, where a, b < 100, what is the 
maximum digital sum?
"""

# let's look at some group theory here.
# we note that digital_sum(a**b) = a % 10 // 1 + a % 100 // 10 + ...

# let's look at this backwards

def digital_sum(n):
    return sum(int(digit) for digit in str(n))
    
maxSoFar = 0
maxA, maxB = 0, 0
for a in range(99, 85, -1):
    for b in range(99, 85, -1):
        digitalSum = digital_sum(a**b)
        if digitalSum > maxSoFar:
            maxSoFar = digitalSum
            maxA, maxB = a, b
            print(maxSoFar)
            print('a={0}, b={1}, digitalSum={2}'.format(a, b, digitalSum))