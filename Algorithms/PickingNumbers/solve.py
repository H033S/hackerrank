#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    x = [0 for i in range(101)]
    resp = 0

    for i in a:
        x[i] += 1
    
    for i in range(1,101):
        resp = max(resp, x[i - 1] + x[i])
    
    print(resp)
        
    




if __name__ == '__main__':
 #   fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

 #   fptr.write(str(result) + '\n')

#    fptr.close()
