# -*- coding: utf-8 -*-


# euler 01: find the sum of all multiples of 3 or 5 below 1000'''
threeMultiples = (x for x in range(0, 1000, 3))
fiveMultiples = (x for x in range(0, 1000, 5))
threeAndFiveMultiples = (x for x in range(0, 1000, 15))

total = sum(threeMultiples) + sum(fiveMultiples) + sum(threeAndFiveMultiples)
print(total)
