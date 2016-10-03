# -*- coding: utf-8 -*-
'''
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1);
 so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and
 adding these values we form a word value. For example, the word value for SKY is
 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call
 the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly 
two-thousand common English words, how many are triangle words?
'''
import csv
from string import ascii_uppercase

def get_value(word):
    value = {char: index for index, char in enumerate(ascii_uppercase, 1)}
    return sum((value[char] for char in word))


triangular = {n*(n+1)//2 for n in range(1, 200)}
def gen_triangular_words():

    with open('p042_words.txt') as text:
        read = csv.reader(text)
        words = (word for line in read for word in line)    
        for word in words:
            value = get_value(word)
            if value in triangular:
                yield word
                

triangularWords = sorted([word for word in gen_triangular_words()], key = get_value)
print(triangularWords)
print('')
print(len(triangularWords))