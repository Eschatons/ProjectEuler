# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 14:53:17 2016

@author: efron
"""


"""
Let p(n) represent the number of different ways in which n coins can be
 separated into piles. For example, five coins can be separated into piles 
 in exactly seven different ways, so p(5)=7.

OOOOO
OOOO   O
OOO   OO
OOO   O   O
OO   OO   O
OO   O   O   O
O   O   O   O   O
Find the least value of n for which p(n) is divisible by one million.
"""

from enumeration import integer_partition as p

def find_first_divisible_by_one_million():
    n = 1
    while True:
        if p[n]% 10**6 == 0:
            return n
        n += 1

n = find_first_divisible_by_one_million()
print(n)