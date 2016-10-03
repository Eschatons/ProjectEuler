# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 13:05:17 2016

@author: efron
"""

"""
Each character on a computer is assigned a unique code and the preferred 
standard is ASCII (American Standard Code for Information Interchange). 
For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to 
ASCII, then XOR each byte with a given value, taken from a secret key.
The advantage with the XOR function is that using the same encryption key on 
the cipher text, restores the plain text; for example, 65 XOR 42 = 107, 
then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text 
message, and the key is made up of random bytes. The user would keep the 
encrypted message and the encryption key in different locations, and without 
both "halves", it is impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the modified 
method is to use a password as a key. If the password is shorter than the 
message, which is likely, the key is repeated cyclically throughout the 
message. The balance for this method is using a sufficiently long password 
key for security, but short enough to be memorable.

Your task has been made easy, as the encryption key consists of three lower 
case characters. Using cipher.txt (right click and 'Save Link/Target As...'), 
a file containing the encrypted ASCII codes, and the knowledge that the plain
text must contain common English words, decrypt the message and find the sum 
of the ASCII values in the original text.
"""

import csv
from string import ascii_lowercase
import re
from itertools import permutations
from collections import namedtuple
def decipher(text):
    def get_code_words():
        with open(text) as cipherText:
            asCSV= csv.reader(cipherText)
            codeWords = [x for line in asCSV for x in line]
        return codeWords
    
    def xor(text, key):
        paddedKey = key * (len(text) // len(key))
        textCodePoints = (int(x) for x in text)
        keyCodePoints = (ord(x) for x in paddedKey)
        chars = (chr(x^y) for x, y in zip(textCodePoints, keyCodePoints))
        chars = ''.join(chars)
        return chars 
        
    def get_top_200_words(filename):
        with open(filename) as text:
            words = (word for line in text for word in line)
            commonWords = [next(words) for n in range(200)]
            return commonWords
    
    commonWords = get_top_200_words('p059_commonEnglishWords.txt')
    
    def count_common_english_words():
        count = 0
        IGNORECASE = 0b10
        ASCII = 0b100000000
        for word in commonWords:
            regex = ''.join((r'\b',word,r'\b'))
            allMatches = re.findall(regex, decipheredText, ASCII | IGNORECASE)
            for match in allMatches:
                count += 1
        return count
        

    codeWords = get_code_words()
    commonWords = get_top_200_words('p059_commonEnglishWords.txt')
    Score = namedtuple('Score', ['key', 'score'])
    scores = []
    for permutation in permutations(ascii_lowercase, 3):
        key = ''.join(permutation)
        decipheredText = xor(codeWords, key)
        score = count_common_english_words()
        scores.append(Score(key, score))
  
    scores.sort(key = lambda x: x.score, reverse=True)
    topFiveScores = scores[:5]
    
    for key, score in topFiveScores:
        print(key, score)
        print(xor(text, key))
    return topFiveScores

        

    
text = 'p059_cipher.txt'

scores = decipher('p059_cipher.txt')