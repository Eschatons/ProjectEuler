# -*- coding: utf-8 -*-

""" what is the 10,001st prime? """


def get_primes_under(n):
    with open('primes.txt') as text:
        for line in text:
            prime, _ = line.split('\n')
            prime = int(prime)
            if prime < n:
                yield prime
            else:
                break
