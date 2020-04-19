#!/bin/python3

import math
import os
import random
import re
import sys

def update(s, lazy, id, l, r, x):
    lazy[id] += x
    s[id] += (r - l) * x

##Pass Update to childrens
def shift(s, lazy, id, l, r):
    mid = (l + r) >> 1

    update(s, lazy, id<<1, l, mid, lazy[id])
    update(s, lazy, id<<1|1, mid + 1, r, lazy[id])
    lazy[id] = 0

##Increase count x to the interval x,y 
def increase(s, lazy, x, y, v, id, l, r):
    if x >= r or l >= y:
        return 
    if x <= l and r <= y:
        update(s, lazy, id, l, r, v)
        return
    
    shift(s, lazy, id, l, r)
    
    mid = (l + r) >> 1
    increase(s, lazy, x, y, v, id<<1, l, mid)
    increase(s, lazy, x, y, v, id<<1|1, mid + 1, r)
    s[id] = s[id << 1] + s[id << 1 | 1]

##Query Answer
def query(s, lazy, x, y, id, l, r):
    if x >= r or l >= y:
        return 0
    if x <= l and r <= y:
        return s[id]
    shift(s, lazy, id, l, r)
    mid = (l + r) >> 1

    return max(
        query(s, lazy, x, y, id<<1, l, mid), 
        query(s, lazy, x, y, id<<1|1, mid + 1, r)
    )
    
# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    s = [0 for x in range(4*n)]
    lazy = [0 for x in range(4*n)]

    for q in queries:
        increase(s, lazy, q[0], q[1], q[2], 1, 0, n)    
    
    return query(s, lazy, 1, n, 1, 0, n)        
    
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []
     

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)
    print(result)

    #fptr.write(str(result) + '\n')

    #fptr.close()
