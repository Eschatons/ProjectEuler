# -*- coding: utf-8 -*-

""" find the difference between the sum of the squares of the first 100 natural numbers and the
square of the sums """

sumOfSquares = sum(x ** 2 for x in range(1, 101))
squareOfSums = sum(x for x in range(1, 101)) ** 2
print(squareOfSums - sumOfSquares)
