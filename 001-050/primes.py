# -*- coding: utf-8 -*-

""" what is the 10,001st prime? """

import bisect
import math
import numpy as np

def sieve_primes_under(n):
    if n < 2:
        raise ('No primes under 2!')
    else:
        primes = [2]
        nonPrimes = np.zeros(n, dtype='bool')
        nonPrimes[3::2] = True
    for i in range(3, n, 2):
        if nonPrimes[i-1] == False:
            primes.append(i)
            nonPrimes[2*i-1::i] = True
    return primes


def gen_primes_under(n):
    with open('primes.txt') as text:
        for line in text:
            prime, _ = line.split('\n')
            prime = int(prime)
            if prime < n:
                yield prime
            else:
                break


def gen_n_primes(n):
    with open('primes.txt') as text:
        counter = 0
        for line in text:
            counter += 1
            prime, _ = line.split('\n')
            prime = int(prime)
            if counter < n:
                yield prime
            else:
                break


def factor_elements(iterable):
    root = math.sqrt(max(iterable))
    primes = sorted(list(gen_primes_under(root)))

    def factor(elem):
        nonlocal primes
        factors = []
        primes = primes
        root = math.sqrt(elem)
        maxPrimeIndex = bisect.bisect_right(iterable, root)
        primeList = primes[:maxPrimeIndex]

        for prime in primeList:
            while elem % prime == 0:
                factors.append(prime)
        return factors

    for elem in iterable:
        yield factor(elem)

