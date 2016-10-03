# -*- coding: utf-8 -*-

"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
from primes import sieve_primes_under

prime_sum = sum(sieve_primes_under(2 * (10 ** 6)))
print(prime_sum)
