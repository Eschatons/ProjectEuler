# -*- coding: utf-8 -*-


import re

def getInts(s):
    lines = re.split('\n', s)
    for line in lines:
        yield [int(x) for x in re.split(' ', line) if x != '']

def max_path_sum(triangle):
    maxSum = [[] for row in triangle]
    for rowIndex, row in enumerate(triangle):
        for colIndex, elem in enumerate(row):
            if rowIndex == 0:
                maxSum[0] = row
            else:
                maxNeighborSum = max(maxSum[rowIndex-1][colIndex], maxSum[rowIndex-1][colIndex+1])
                maxSum[rowIndex].append( maxNeighborSum + elem)
    return maxSum
    

def Tree:
    