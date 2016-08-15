
"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""
from math import factorial


# let's look at some bounds. note
# 9! = 362880
# 999999! = sum(factorial(9) for _ in range(6)) = 2177280
# so we only need to examine things between 0 and 2*10**6

digitFactorialSums = []
for n in range(3, 2*10**6):
    if n == sum(factorial(int(digit)) for digit in str(n)):
        digitFactorialSums.append(n)
print(sum(digitFactorialSums))