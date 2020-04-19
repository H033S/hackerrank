#Este es el que subi en hackerrank
#!/bin/python3

import math
import os
import random
import re
import sys

global s
global lazy

def shift(id, l, r):
    mid = (l + r) >> 1

    lazy[id<<1] += lazy[id]
    lazy[id<<1|1] += lazy[id]

    s[id<<1] += lazy[id]
    s[id<<1|1] += lazy[id]
    
    lazy[id] = 0

def update(x, y, v, id, l, r):
    if x > r or l > y:
        return
    if x <= l <= r <= y:
        s[id] += v
        lazy[id] += v
        return
    
    shift(id, l, r)

    mid = (l + r) >> 1
    update(x, y, v, id<<1, l, mid)
    update(x, y, v, id<<1|1, mid + 1, r)
    s[id] = max(s[id << 1], s[id << 1|1])

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):    
    for q in queries:
        increase(q[0], q[1], q[2], 1, 1, n)    

    return s[1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []
    s = [0]*(4*n)
    lazy = [0]*(4*n)

    for _ in range(m):
        inp = list(map(int, input().rstrip().split()))
        update(inp[0], inp[1], inp[2], 1, 1, n)

    fptr.write(str(s[1]) + '\n')

    fptr.close()
