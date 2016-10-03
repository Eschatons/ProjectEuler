# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 14:51:50 2016

@author: efron
"""
def _make_stirling2():
    """ factory function that produces stirling2"""
    seen = {(0, 0): 1}
    def stirling2(n: int, k: int) -> int:
        """ stirling number of the second kind. useful for counting surjections
        of n objects onto k distinct boxes, where
        surjections(n, k) = S(n, k)*k!"""
        nonlocal seen
        
        if k > n:
            return 0
        key = n, k
        if key in seen:
            return seen[key]
        seen[n, k] = stirling2(n-1, k-1)+k*stirling2(n-1, k)
    return stirling2

stirling2 = _make_stirling2()