# -*- coding: utf-8 -*-

def digit_sum(n):
    total = 0
    for char in str(n):
        total += int(char)
    return total


def digit_factorial(n):
    total = 0
    for char in str(n):
        total += factorial(int(char))
    return total


def factorial(n):
    total = 1
    for i in range(2, n + 1):
        total *= i
    return total
