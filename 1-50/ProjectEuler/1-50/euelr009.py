# -*- coding: utf-8 -*-

"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a**2 + b**2 = c**2
For example, 3**2 + 4**2 == 9 + 16 == 25 = 5**2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
def is_pythagorean_triplet(a, b, c):
    if a**2 + b**2 == c**2:
        return True
    else:
        return False

print(is_pythagorean_triplet(3, 4, 5))
def find_pythagorean_triplet():
    for c in range(1000, 1, -1):
        for a in range(1, c):
            b = max(1, 1000-c-a)            
            if is_pythagorean_triplet(a, b, c):
                return (a, b, c)
    
    return None, None, None
(a, b, c) = find_pythagorean_triplet()
print(a, b, c)