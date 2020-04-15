#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    valleys = 0
    level = 0

    for stp in s:
        if stp == 'U':
            if not level + 1:
                valleys += 1
            level += 1
        if stp == 'D':
            level -= 1
    
    return valleys


if __name__ == '__main__':
  #  fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)
    print(result)

   # fptr.write(str(result) + '\n')

#    fptr.close()
