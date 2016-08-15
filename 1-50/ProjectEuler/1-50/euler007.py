# -*- coding: utf-8 -*-

""" what is the 10,001st prime? """

from primes import sieve_primes_under

primes = sieve_primes_under(10**6)
print(primes[10000])