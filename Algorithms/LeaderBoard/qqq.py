#!/bin/python3

import math
import os
import random
import re
import sys

def binarySearch(num,arr):
    _min,_max = 0, len(arr)

    while(_min < _max):
        med = (_min + _max)//2

        if num < arr[med]:
            _min = med + 1
        elif num >= arr[med]:
            _max = med
    return _max + 1

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    scrs = []
    scrs.append(scores[0])
    resp = []
    
    for i in range(1,len(scores)):
        if scrs[-1] == scores[i]:
            continue
        scrs.append(scores[i])
    
    for gam_scr in alice:
        resp.append(binarySearch(gam_scr,scrs))

    return resp


    
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
