#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    l = len(s)
    #number of a's from i position
    a = [0 for x in range(l)]

    count = 0
    for i in range(l):
        if s[i] == 'a':
            count += 1 
        a[i] = count

    result = n // l * a[l - 1] 
    
    rest = n % l
    if not rest:
        return result

    return result + a[rest - 1]      


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    print(result)
    #fptr.write(str(result) + '\n')

    #fptr.close()
