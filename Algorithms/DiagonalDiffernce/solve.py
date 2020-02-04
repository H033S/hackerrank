#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    ind = len(arr)-1
    d1, d2 = 0, 0

    for i in range(len(arr)):
        d1 += arr[i][i]
        
        d2 += arr[ind][i]
        ind -= 1

    return int(math.fabs(d1 - d2))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)
    
    fptr.write(str(result) + '\n')

    fptr.close()
