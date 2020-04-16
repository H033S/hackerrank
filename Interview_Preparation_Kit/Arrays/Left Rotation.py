#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    new_a = []
    step_count = 0

    i = d
    while step_count < len(a):
        new_a.append(a[i])
        i = (i + 1) % len(a)
        step_count += 1
    
    return new_a

if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)
    print(result)

    #fptr.write(' '.join(map(str, result)))
    #fptr.write('\n')

   # fptr.close()
