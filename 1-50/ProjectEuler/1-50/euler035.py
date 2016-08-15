# -*- coding: utf-8 -*-

''''
The number, 197, is called a circular prime because all rotations of the digits:
 197, 971, and 719, are themselves prime.
There are thirteen such primes below 100: 
2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
How many circular primes are there below one million?
'''

from primes import sieve_primes_under

def gen_circular_primes(primes = sieve_primes_under(10**6)):
    def rotateForward(string):
        return string[1:]+string[0]
    def rotateBack(string):
        return string[-1]+string[:-1]
    primes = {str(prime) for prime in primes}
    for prime in primes:
        circular = True
        forward, back = prime, prime
        for index, _ in enumerate(prime):
            forward = rotateForward(forward)
            back = rotateBack(back)
            if (forward not in primes) or (back not in primes):            
                circular = False
                break
        if circular:
            yield int(prime)

circular_primes = sorted(list(gen_circular_primes()))
print(circular_primes)
print(len(circular_primes))
