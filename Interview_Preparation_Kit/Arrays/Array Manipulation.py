#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    arr = [0]*(n+1)

    for a, b, v in queries:
        arr[a] += v

        if b + 1 <= n:
            arr[b + 1] -= v
    
    mx , sm = 0, 0
    for it in arr:
        sm += it
        mx = max(sm, mx)
    
    return mx

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)
    print(result)
    #fptr.write(str(result) + '\n')

    #fptr.close()
