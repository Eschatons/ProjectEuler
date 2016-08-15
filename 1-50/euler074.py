"""
The number 145 is well known for the property that the sum of the factorial of its
 digits is equal to 145:

1! + 4! + 5! = 1 + 24 + 120 = 145

Perhaps less well known is 169, in that it produces the longest chain of numbers that 
 link back to 169; it turns out that there are only three such loops that exist:

169 → 363601 → 1454 → 169
871 → 45361 → 871
872 → 45362 → 872

It is not difficult to prove that EVERY starting number will eventually get stuck in a loop.
 For example,

69 → 363600 → 1454 → 169 → 363601 (→ 1454)
78 → 45360 → 871 → 45361 (→ 871)
540 → 145 (→ 145)

Starting with 69 produces a chain of five non-repeating terms, but the longest non-repeating chain
with a starting number below one million is sixty terms.

How many chains, with a starting number below one million, 
contain exactly sixty non-repeating terms?"""

from eulerHelpers import factorial


def digit_factorial(n):
    total = 0
    for char in str(n):
        total += factorial(int(char))
    return total


def digit_factorial_chain(n):
    chain = set()
    trials = 0
    while n not in chain:
        trials += 1
        chain |= {n}
        n = digit_factorial(n)
    return chain


sixtyNonRepeating = 0
badChains = set()
goodChains = set()
for n in range(1, 10 ** 6):
    if not (n in goodChains or n in badChains):
        chain = digit_factorial_chain(n)
        if len(chain) == 60:
            sixtyNonRepeating += 1
            # print (chain - goodChains)
            goodChains |= {n for n in chain}
        else:
            badChains |= {n for n in chain}
print(sixtyNonRepeating)
