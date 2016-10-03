""" what is the smallest positive number that is evenly divisble by n in range(1, 21)? """

' we note max prime divisors in 0<n<21 are 2**4: 16, 3*2 (9), 5, 7, 11, 13, 17, 19'

total = (2 ** 4) * (3 ** 2) * 5 * 7 * 11 * 13 * 17 * 19
print(total)
