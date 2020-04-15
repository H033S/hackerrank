#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'longestSubarray' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def longestSubarray(arr):
    arr.sort()
    mark = {}
    s = 0

    for i in range(len(arr)-1,-1,-1):
        if not mark.__contains__(arr[i]):
            mark.update({arr[i]:1})
            s += arr[i]
    
    return s

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = longestSubarray(arr)

    #fptr.write(str(result) + '\n')

    #fptr.close()
