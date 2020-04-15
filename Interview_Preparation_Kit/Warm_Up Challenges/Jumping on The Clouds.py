#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    jumps = 0
    
    i = 0
    while i < len(c)-1 :
        #it's in and it isn't thundercloud
        if i+2 < len(c) and not c[i+2]:
            i += 2
            jumps += 1
            continue
        if i+1 < len(c) and not c[i+1]:
            jumps += 1
            i += 1

    return jumps
        

if __name__ == '__main__':
   # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)
    print(result)
    #fptr.write(str(result) + '\n')

    #fptr.close()
