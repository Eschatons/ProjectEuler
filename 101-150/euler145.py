# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 11:53:32 2016

@author: efron
"""

"""Some positive integers n have the property that the sum [ n + reverse(n) ] 
consists entirely of odd (decimal) digits. For instance, 36 + 63 = 99 and 
409 + 904 = 1313. We will call such numbers reversible; so 36, 63, 409, and 
904 are reversible. Leading zeroes are not allowed in either n or reverse(n).

There are 120 reversible numbers below one-thousand.

How many reversible numbers are there below one-billion (109)?
"""

# we note a couple rules to cut down the stuff we have to examine
# if the leading digit is even and the second digit <= 4, we can cut it out
# if the final digit is even we can't get a reversible

def get_reverse(n):
    s = str(n)

    return int(s[::-1])

def is_reversible(n):
    odds = {'1', '3', '5', '7', '9'}
    reverse = get_reverse(n)
    if reverse is None:
        return False
    total = n + reverse
    if set(str(total)) <= odds:
        return True
    return False
    

ranges = ((.44, 1), (1, 2), (2.44, 3),
          (3, 4), (4.44, 5), (5, 6), 
            (6.44, 7), (7, 8), (8.44, 8), (9, 10))

candidates = ()
def gen_candidate():
    for k in range(9):
        for start, end in ranges:
            start = round((10**k)*start)
            end = round((10**k)*end)
            for n in range(start+1, end, 2):
                yield n
                
candidates = gen_candidate()

reversibles = (n for n in candidates if is_reversible(n))
print(reversibles)
reversibleCount = 0
for n in reversibles:
    reversibleCount += 1
    if reversibleCount % 1000 == 0:
        print(n)