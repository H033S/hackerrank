#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    new_arr = [x-1 for x in arr]
    positions = [0 for x in arr]
    count = 0
    
    for i, x in enumerate(new_arr):
        positions[x] = i
    
    for i in range(len(new_arr)):
        if positions[i] == i:
            continue
        
        num = new_arr[i]
        
        (new_arr[i] , new_arr[positions[i]]) = (new_arr[positions[i]], new_arr[i])
        (positions[i], positions[num]) = (positions[num], positions[i])
        count += 1
    
    return count
            

if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)
    print(res)

#    fptr.write(str(res) + '\n')

#    fptr.close()
