# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 10:40:08 2016

@author: efron
"""

# euler079
"""
A common security method used for online banking is to ask the user for
three random characters from a passcode. For example, if the passcode was
531278, they may ask for the 2nd, 3rd, and 5th characters; the expected
 reply would be: 317.

The text file, keylog.txt, contains fifty successful login attempts.

Given that the three characters are always asked for in order, analyse
 he file so as to determine the shortest possible secret passcode
of unknown length.
"""
import re
with open('p079_keylog.txt') as text:
    keys = [line for line in text]

keys = [re.sub('\n', '', line) for line in keys]

digits = set(x for line in keys for x in line)
right = {digit: set() for digit in digits}
left = {digit: set() for digit in digits}


for line in keys:
    
    first, middle, last = line

    right[first] |= {middle, last}
    right[middle] |= {last}

    left[middle] |= {first}
    left[last] |= {middle, first}
    

# ordered:
leftKeys = sorted(digits, key = lambda x: len(left[x]))
rightKeys = sorted(digits, key = lambda x: len(right[x]), reverse = True)

print('left')
for x in leftKeys:
    print(x, left[x])
print('\nright')
for x in rightKeys:
    print(x, right[x])
leftSol = ''.join(leftKeys)
rightSol = ''.join(rightKeys)

if leftSol == rightSol:
    solution = leftSol
    print(solution)
