# -*- coding: utf-8 -*-

import re

with open('reversed_primes.txt') as read:
    primes = [re.sub(line, '\n', '') for line in read if line != '\n']
with open('reversed_primes.txt', 'w') as write:
    for prime in primes:
        print(prime, file=write)
