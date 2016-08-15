# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 17:39:34 2016

@author: efron
"""

with open('primes.txt') as text:
    n = 0
    for line in reversed(text):
        print(line)
        n += 1
        if n > 5:
            break
