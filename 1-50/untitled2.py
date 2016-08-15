# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 16:22:56 2016

@author: efron
"""
""" find the last ten digits of 
28433*2**7830457"" + 1 """

power = 7830457

n = 1
for n in range(power):
    n *= 2
    n %= 10 ** 10
n *= 28433
n %= 10 ** 10
n += 1

print(n)
