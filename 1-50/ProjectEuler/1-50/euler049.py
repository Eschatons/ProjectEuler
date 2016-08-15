# -*- coding: utf-8 -*-

'''The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, 
is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers
 are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, 
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
'''

from primes import sieve_primes_under
from bisect import bisect
from itertools import permutations
primes = sieve_primes_under(10000)
primes = primes[bisect(primes, 999):]
primeStrings = {str(x) for x in primes}

def permuted_primes(primes = primes):
    for prime in primeStrings:
        permuted = (''.join(x) for x in permutations(prime))
        rotations = sorted(list({int(x) for x in permuted if x in primeStrings}))
        if len(rotations) == 3:
            yield(tuple(rotations))
                
permuted = permuted_primes()

for rotations in sorted(list(set(permuted))):
    difference = 0, rotations[1]-rotations[0], rotations[2]-rotations[1]
    print(rotations, difference)
    if difference[2] - difference[1] == difference[1]:
        print(difference)