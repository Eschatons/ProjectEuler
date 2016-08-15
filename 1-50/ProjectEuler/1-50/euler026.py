# -*- coding: utf-8 -*-
'''
A unit fraction contains 1 in the numerator. 
The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle.
 It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d c
ontains the longest recurring cycle in its decimal fraction part.'''

def mult_group(n, *, mod):
    seen = set()
    k = n
    while k not in seen:
        k %= mod
        seen |= {k}
        k *= n
    return seen

sharedDivisors = set(range(2, 1000, 2)) | set(range(5, 1000, 5))
relativelyPrime = sorted(list(set(range(2, 1000)) - sharedDivisors))
maxLen = 0
bestSoFar = 0
for n in relativelyPrime[50:]:
    group= mult_group(10, mod=n)
    if len(group)> maxLen:
        maxLen, bestSoFar = len(group), n
        bestGroupSoFar = group

print (maxLen)
print (bestSoFar)
print (sorted(list(bestGroupSoFar)))