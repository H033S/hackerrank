#!/bin/python3

import math
import os
import random
import re
import sys

r = [0 , 0 , 0 , 1 , 2 , 2 , 2]
c = [0 , 1 , 2 , 1 , 0 , 1 , 2] 

def calculate_sum_hourglass(arr, i, j):
    _sum = -100

    for k in range(len(r)):
        _sum += arr[i + r[k]][j + c[k]]
    
    return _sum

# Complete the hourglassSum function below.
def hourglassSum(arr):
    max_hourglass = 0

    for i in range(4):
        for j in range(4):
            max_hourglass = max(
                max_hourglass,
                calculate_sum_hourglass(
                    arr, i , j
                )
            )
    
    return max_hourglass
        
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)
    print(result)
    #fptr.write(str(result) + '\n')

    #fptr.close()
