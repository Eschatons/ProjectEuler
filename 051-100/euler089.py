# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 14:23:14 2016

@author: efron
"""
from csv import reader
with open('p089_roman.txt') as text:
    asCSV = reader(text)
    romanNumerals = tuple(word for line in asCSV for word in line)

values = {'I': 1, 'V': 5, 'X': 10, 
          'L': 50, 'C': 100, 'D': 500, 
          'M':1000, None: 0
          }

def parse_roman_numeral(roman):
    total  = 0
    skipNext = False
    for i, char in enumerate(roman):
        if skipNext:
            skipNext = False
        else:
            try: 
                nextChar = roman[i+1]
            except IndexError:            # end of numeral
                nextChar = None
            val, nextVal = values[char], values[nextChar]
            if nextVal > val:
                total += (nextVal - val)
                skipNext = True
            else:
                total += val
    return total
    
def create_minimum_numeral(value):
    remaining = value
    roman = []
    # thousands
    while remaining > 1000:
        roman.append('M')
        remaining -= 1000
        
    #hundreds
    if remaining // 100 == 9:
        roman.append('C')
        roman.append('M')
        remaining -= 900
    if remaining >= 500:
        roman.append('D')
        remaining -= 500
    if remaining // 100 == 4:
        roman.append('C')
        roman.append('D')
        remaining -= 400
    while remaining >= 100:
        roman.append('C')
        remaining -= 100
    if remaining // 10 == 9:
        roman.append('X')
        roman.append('C')
        remaining -= 90
    # tens
    if remaining // 10 >= 5:
        roman.append('L')
        remaining -= 50
    if remaining // 10 == 4:
        roman.append('X')
        roman.append('L')
        remaining -= 40
    while remaining >= 10:
        roman.append('X')
        remaining -= 10
    
    # ones
    if remaining == 9:
        roman.append('I')
        roman.append('X')
        remaining -= 9
    if remaining >= 5:
        roman.append('V')
        remaining -= 5
    if remaining == 4:
        roman.append('I')
        roman.append('V')
        remaining -= 4
    while remaining > 0:
        roman.append('I')
        remaining -= 1
    
    roman = ''.join(roman)
    return roman

values = tuple(parse_roman_numeral(x) for x in romanNumerals)
minimumRomanNumerals = tuple(create_minimum_numeral(value) for value in values)
totalSaved = 0
for roman, minimumRoman, value in zip(romanNumerals, minimumRomanNumerals, values):
    saved = len(roman) - len(minimumRoman)
    print('{0} = {1} <--> {2}'.format(value, roman, minimumRoman))
    totalSaved += saved
print(totalSaved)
    