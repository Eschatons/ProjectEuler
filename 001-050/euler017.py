# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 09:49:57 2016

@author: efron
"""
# euler 017
'''
If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out 
in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 
(three hundred and forty-two) contains 23 letters and 115
(one hundred and fifteen) contains 20 letters. The use of "and" when
writing out numbers is in compliance with British usage.
'''

def nums_to_words(n: int) -> str:
    ones = {0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
            5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}

    teens = {10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen',
             14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen',
             18: 'eighteen', 19: 'nineteen'}
             
    tens = {0: '', 1: NotImplementedError, 2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty',
            7: 'seventy', 8: 'eighty', 9: 'ninety'}
            
    def thousands(n: int) -> str:
        kPlace = n // 1000
        if kPlace > 0:
            kStr = ones[kPlace] +'thousand'
        else:
            kStr = ''
        return kStr
        
    def hundreds(n: int) -> str:
        hPlace = (n % 1000) // 100
        if hPlace > 0:
            hStr = ones[hPlace]
            hStr += 'hundred'
            if n % 100 != 0:
                hStr += 'and'
        else:
            hStr = ''
        return hStr
    
    def teens_and_ones(n: int) -> str:
        n %= 100
        if 9 < n and n < 20:
            toStr = teens[n]
        elif n <= 9:
            toStr = ones[n]
        else:
            tPlace = n // 10
            oPlace = n % 10
            toStr = tens[tPlace] + ones[oPlace]
        return toStr
    
    return thousands(n) + hundreds(n) + teens_and_ones(n)


asWords = [nums_to_words(n) for n in range(1, 1001)]
print(asWords)
lengths = (len(n) for n in asWords)
lenSum = sum(lengths)