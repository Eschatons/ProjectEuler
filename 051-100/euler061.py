# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 10:09:55 2016

@author: efron
"""
from typing import Callable, List

def triangular(n: int) -> int:
    return (n*n+1)//2
    
def square(n: int) -> int:
    return n**2
    
def pentagonal(n: int) -> int:
    return (n*(3*n-1))//2
    
def hexagonal(n: int) -> int:
    return n*(2*n-1)
    
def heptagonal(n: int) -> int:
    return n*(5*n-3)/2
    
def octagonal(n: int) -> int:
    return n*(3*n-2)

def get_four_digit_elems(func: Callable) -> List[str]:
    n = 1
    fn = func(n)
    fourDigitElems = []
    while fn < 10**5:
        if fn >= 1000:
            fourDigitElems.append(str(fn))
        n += 1
        fn = func(n)
    return fourDigitElems

figurate_functions = [triangular, square, pentagonal,
                      hexagonal, heptagonal, octagonal]
figurates = [get_four_digit_elems(function) for function in figurate_functions]

triangles, squares, pentagons, hexagons, heptagons, octagons = figurates
print(triangles)
