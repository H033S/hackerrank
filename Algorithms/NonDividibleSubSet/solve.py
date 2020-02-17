#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, s):
    rests = [0 for x in range(k)]
    result = 0

    for x in s:
        rests[x%k] += 1

    for i in range(1, k//2 + 1):
        result += max(rests[i], rests[k - i])
    
    if not k % 2:
        result +=  min(1, rests[k//2]) - rests[k//2]
    
    return result + min(1, rests[0])

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)
    print(result)
    #fptr.write(str(result) + '\n')

    #fptr.close()
