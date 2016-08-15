# -*- coding: utf-8 -*-

""" what is the 10,001st prime? """
import bisect
from collections import Counter
import itertools
import math
import numpy as np
from random import randint
from typing import List

def miller_rabin(n: int) -> bool:
    """ stochastic test to determine primality of n. 
    True --> n is most likely prime
    False --> n is definitely composite """
    s = n-1
    t = 0
    while s & 1 | 0 == 0:   # while s % 2 == 0
        s //= 2        
        t += 1
    
    for trials in range(5):    
        base = randint(2, n-2)
        v = pow(base, s, n)
        if v != 1:
            i = 0
            while v != n-1:
                if i == t-1:
                    return False
                else:
                    i = i+1
                    v = (v**2) % n
    return True
    
def is_prime(n):
    """ stochastic test to determine primality of n.
    tests for divisibility by low primes, then invokes miller rabin primality test to 
    more thoroughly check probability space.
    True --> n is most likely prime
    False --> n is definitely composite"""
    
    lowPrimes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
             73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157,
             163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241,
             251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 
             349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443,
             449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563
             }
    
    if n in lowPrimes:
        return False
    
    for prime in lowPrimes:
        if n % prime == 0:
            return False
    else:
        return miller_rabin(n)

def product(iterable):
    product = 1
    for i in iterable:
        product *= i
    return product
    
def sieve_primes_under(n: int) -> List:
    if n < 3 or n != math.floor(n):
        raise ValueError('input should be a positive int 3 or greater')
    nonPrimes = np.zeros(n, dtype = 'bool')
    nonPrimes[3::2] = True
    primes = [2]
    for i in range(3, n):
        if nonPrimes[i-1] == 0:
            nonPrimes[(i*2)-1::i] = True
            primes.append(i)
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


def unique_factorization(n: int, *, primes = None) -> Counter:
    if primes is None:
        primes = sieve_primes_under(n)
    else:
        index = bisect.bisect_right(primes, n)
        primes = primes[:index]
    
    factors = []
    
    for prime in primes:
        while n % prime == 0:
            factors.append(prime)
            n /= prime
        if n == 1:
            break
    else:                        # last element is itself a prime
        factors.append(n)
    return Counter(factors)

    
def totient(n: int, *, primes = None) -> int:
    factors = unique_factorization(n, primes = primes)
    totient = 1
    for prime in factors:
        totient *= prime**factors[prime] - prime**(factors[prime]-1)
    return totient
    
def z_star(n, primes = None):
    notRelativelyPrime = set()
    factors = unique_factorization(n, primes = primes)
    for factor in factors:
        multiples = set(range(factor, n, factor))
        notRelativelyPrime |= multiples
    zStar = set(range(n)) - notRelativelyPrime
    return frozenset(zStar)
    
    
def multiplicative_group_n_mod_k(n: int, k: int) -> List:
    seen = set()
    i = n
    while i not in seen:
        i %= k
        seen |= {i}
        i *= n
    return sorted(list(seen))

def divisors(n: int, primes = None) -> List:
    factors = unique_factorization(n, primes = primes)
    factors = [x for x in factors for y in range(factors[x])]
    divisors = []
    for i in range(len(factors)):
        for j in itertools.combinations(factors, i):
            divisors.append(product(j))
    
    return sorted(list(set(divisors)))
    

    

def count_divisors(n: int, primes = None) -> int:
    factors  = unique_factorization(n, primes = primes)
    return product(factors[x]+1 for x in factors)
