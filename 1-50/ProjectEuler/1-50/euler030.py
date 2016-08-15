# -*- coding: utf-8 -*-


"""
Surprisingly there are only three numbers that can be written
 as the sum of fourth powers of their digits:

1634 = 1**4 + 6**4 + 3**4 + 4**4
8208 = 8**4 + 2**4 + 0**4 + 8**4
9474 = 9**4 + 4**4 + 7**4 + 4**4
As 1 = 1**4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the 
sum of fifth powers of their digits.
"""

# let's examine the possible range.
# we note that 9**5 = 59049
# so then we can have at most six digits, since
# 999999 --- > 6**(9**5) == 354294

from itertools import accumulate
def power_digit_sum(n, *, power):
    return sum(int(digit)**power for digit in str(n))

digit_fifth_powers = []
for n in range(2, 354294):
    if n == power_digit_sum(n, power = 5):
        digit_fifth_powers.append(n)
print(digit_fifth_powers)
print([x for x in accumulate(digit_fifth_powers)])