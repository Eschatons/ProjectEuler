# -*- coding: utf-8 -*-

'''
If the numbers 1 to 5 are written out in words: one, two, three, four, five,
 then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
'''

def num_to_word(n, *, spaces = False):
    
    hundredDict = {0: '', 1: 'one', 2: 'two', 3: 'three',
                       4: 'four', 5: 'five', 6: 'six',
                       7: 'seven',  8: 'eight', 9: 'nine'}
    tenDict = {0: '', 2: 'twenty', 3: 'thirty', 4: 'forty',
            5: 'fifty',  6: 'sixty', 7:'seventy',
            8:'eighty',  9: 'ninety'}
            
    teenDict = {10: 'ten', 
            11: 'eleven', 12: 'twelve', 13: 'thirteen',
            14: 'forteen', 15: 'fifteen', 16: 'sixteen',
            17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
            
    oneDict = {0: '',     
               1: 'one', 2: 'two', 3: 'three',
               4: 'four',  5: 'five', 6: 'six',
               7: 'seven', 8: 'eight', 9: 'nine'}
    
    string = []
    thousand = n // 1000
    hundred = (n % 1000) // 100
    remainder = n % 100
    if hundred > 0:
        string.append(hundredDict[hundred])
        string.append('hundred')
        if remainder > 0:
            string.append('and')
    
    if 9 < remainder < 20:
        string.append(teenDict[remainder])
        
    else:
        string.append(tenDict[remainder // 10])
        string.append(oneDict[remainder % 10])
    
    if spaces:
        string = ' '.join(string)
    else:
        string = ''.join(string)
    return string
    
words = [num_to_word(n) for n in range(1, 1000)]
words.append('onethousand')

wordLen = sum((len(word) for word in words))

print(wordLen)
