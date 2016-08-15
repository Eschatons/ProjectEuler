# -*- coding: utf-8 -*-

'''2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2**1000? '''

# python coerces to variable-length ints when necessary. so we can just do as simple operation
from factorial import digit_sum

print(digit_sum(2**1000))