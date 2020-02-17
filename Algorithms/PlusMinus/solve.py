#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the plusMinus function below.
def plusMinus(arr):
    pos, neg, zer = 0, 0, 0

    for x in arr:
        if x > 0:
            pos += 1
            continue
        if x < 0: 
            neg += 1
            continue
        zer += 1

    l = len(arr)

    print('%.6f'% (pos/l))
    print('%.6f'% (neg/l))
    print('%.6f'% (zer/l))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
