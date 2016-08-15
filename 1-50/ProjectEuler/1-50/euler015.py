# -*- coding: utf-8 -*-

'''
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
 there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20×20 grid?
'''

# this is the same as asking what are the permutations created from the characters
#{D: 20, R: 20}.

# this is (10+10)! / (10!)(10!)
# al

from math import factorial

routes = factorial(40) //     (factorial(20) *  factorial(20))
print(routes)

# explicit (bad) way to do 5x5 grid:
from itertools import permutations
routes = sorted(list(set(permutations(['R', 'D']*5))))
routes = [''.join(permutation) for permutation in routes]
print(routes)
print(len(routes))
print( (factorial(10) // (factorial(5) * factorial(5))))