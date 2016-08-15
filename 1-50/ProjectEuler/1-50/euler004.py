'''A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.'''

def is_palindrome(n):
    s = str(n)
    if s == s[::-1]:
        return True
    else:
        return False

def largest_palindrome():
    maxSoFar = 0
    for n in range(1000, 99, -1):
        for m in range(1000, n-1, -1):
            test = n*m
            if test >  maxSoFar and is_palindrome(test):
                a, b, maxSoFar = n, m, test
    return a, b, maxSoFar
a, b, palindrome = largest_palindrome()
print(a, b, palindrome)