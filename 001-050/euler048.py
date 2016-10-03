# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 10:30:51 2016

@author: efron
"""

#euler 048
'''
The series, 1**1 + 2*82 + 3**3 + ... + 10**10 = 10405071317.

Find the last ten digits of the series, 1**1 + 2**2 + 3**3 + ... + 1000**1000.
'''

import formatter
# we note that the last ten digits is the answer mod 10**10

series = []
total = 0
for n in  range(1, 1000):
    power = pow(n, n, 10**10)
    total += power
    total %= 10**10
    series.append(power)

print(series)
print(total)