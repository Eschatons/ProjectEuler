# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 14:53:33 2016

@author: efron
"""

"""
It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at 
least two positive integers?
"""
from enumeration import integer_partition

def nontrivial_partitions(n):
    return integer_partition[n]-1

answer = nontrivial_partitions(100)
print(answer)