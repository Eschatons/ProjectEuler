# -*- coding: utf-8 -*-

def fibbonaci():
    lastfib, fib = 0, 1
    yield fib

    while True:
        lastfib, fib = fib, lastfib + fib
        yield fib


def fibbonaci_under(n):
    lastfib, fib = 0, 1
    yield fib

    while fib < n:
        lastfib, fib = fib, lastfib + fib
        yield fib


def factorial(n):
    total = 1
    for i in range(2, n + 1):
        total *= i
    return total
