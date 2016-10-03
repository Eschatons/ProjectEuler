# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 14:57:17 2016

@author: efron
"""

"""
A number chain is created by continuously adding the square of the digits in a 
number to form a new number until it has been seen before.

For example,

44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless
loop. What is most amazing is that EVERY starting number will eventually 
arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?
"""
from collections import Counter
def check_digit():
    def digit_square(n):
        total = 0
        for char in str(n):
            total += int(char)**2
        return total
        
    seen = {1: 1, 89: 89}
    for n in range(1, 10**7):
        if n % 1000 == 0:
            print(n)
        chain = []
        destination = None
        while True:
            chain.append(n)
            n = digit_square(n)
            if n in seen:
                destination = seen[n]
                break
        if destination is not None:
            for k in chain:
                seen[k] = destination
    results = (seen[n] for n in seen)
    return Counter(results)


answer = check_digit()
print(answer)