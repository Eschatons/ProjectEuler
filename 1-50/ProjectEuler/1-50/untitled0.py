# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 17:41:28 2016

@author: efron
"""

with open('primes.txt') as read:
    with open('reversed_primes.txt', 'w') as write:
        primes = [prime for prime in read]
        for prime in reversed(primes):
            print(prime, file=write)
