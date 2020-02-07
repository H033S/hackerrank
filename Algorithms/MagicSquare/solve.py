#!/bin/python3

from math import fabs
import os
import random
import re
import sys

def valid(p):
    return (
        #rows
        p[0] + p[1] + p[2] == 15 and 
        p[3] + 5 + p[4] == 15 and
        p[5] + p[6] + p[7] == 15 and
        #columns
        p[0] + p[3] + p[5] == 15 and
        p[1] + 5 + p[6] == 15 and
        p[2] + p[4] + p[7] == 15 and
        #diagonals
        p[0] + 5 + p[7] == 15 and
        p[5] + 5 + p[2] == 15 
    )

def getCost(s, permt):
    return int(
        fabs(s[0][0] - permt[0]) + 
        fabs(s[0][1] - permt[1]) + 
        fabs(s[0][2] - permt[2]) +
        fabs(s[1][0] - permt[3]) +
        fabs(s[1][1] - 5) +
        fabs(s[1][2] - permt[4]) + 
        fabs(s[2][0] - permt[5]) +
        fabs(s[2][1] - permt[6]) +
        fabs(s[2][2] - permt[7])     
    )

def perm(arr, permt, result):
    if not len(arr):
        result.append(permt)
    else:
        for i in range(len(arr)):
            perm(arr[:i] + arr[(i+1):], permt + [arr[i]],result)
            
           
def formingMagicSquare(s):
    min_cost = 9999999999999
    resp = []
    perm([1,2,3,4,6,7,8,9], [], resp)
    
    for p in resp:
        if not valid(p):
            continue

        min_cost = min(
            min_cost, getCost(s, p))
    return min_cost
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)
    fptr.write(str(result) + '\n')

    fptr.close()
