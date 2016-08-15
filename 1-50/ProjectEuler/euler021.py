""" amicable numbers. let d(n) be the sum of proper divisors of n. 
we say amicable(a) == True if there exists b such that
     d(a) == b and d(b) == a.
what is the sum of all the amicable numbers under 10000?
"""

from primes import divisors, sieve_primes_under

def amicable_partner(a):
    b = sum(divisors(a))
    if b not in seen and a == sum(divisors(b)):
        return b
    else:
        return None

primes = sieve_primes_under(10000)
seen = set()
amicable = set()
for a in range(2, 10000):
    print(a)
    if a not in seen:
        b = sum(divisors(a, primes = 10000))
        if b not in seen and b != a and sum(divisors(b, primes = 10000)) == a:
            amicable |= {a, b}
        seen |= {a, b}

