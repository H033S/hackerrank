#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    ans = 0
    Q = [P - 1 for P in q]
    greaters = [0 for x in q]
    bribes = 0

    for i in range(len(Q)):

        for j in range(i + 1 ,len(Q)):
            if Q[i] > Q[j]:
                if greaters[i] == 2:
                    print('Too Chaotic')
                    return
                    
                greaters[i] += 1
                bribes += 1
    print(bribes)


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
