#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the aVeryBigSum function below.
def aVeryBigSum(ar):
    carry = 0
    col_sum = 0
    resp = []

    for i in range(len(ar[0]) - 1, 0 , -1):
        for j in range(ar):
            col_sum += ar[i][j]
        col_sum += carry
        carry = col_sum / 10
        resp.insert(0, col_sum % 10)
    
    if carry:
        resp.insert(0, carry)
    
    return resp
            


    

if __name__ == '__main__':
  #  fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)

 #   fptr.write(str(result) + '\n')

#    fptr.close()
