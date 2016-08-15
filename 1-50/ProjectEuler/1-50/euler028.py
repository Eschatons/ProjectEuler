# -*- coding: utf-8 -*-

"""
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral
 is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral 
formed in the same way?

"""

# We note that the corners of a nxn square are determined as follows:
# sum(corners) = 4*(n**2) - 4*(n-1)
# if we think of the top right corner as the 'start' of the spiral
# and subtract one, going counterclockwise around


def diag_values(k):
    if k == 1:
        return 1
    else:
        return 4*(k**2)- (6*(k-1))

corners = (diag_values(x) for x in range(1, 1001, 2))
total = sum(corners)
print(total)