import math
import os
import random
import re
import sys

def binary_conv(n):
    r = []
    
    while n > 0:
        r.append(n % 2)
        n //= 2 

    return r   

def sol(r):
    max_1 = 0
    count = 0

    for i in range(len(r)):
        if not r[i]:
            continue
        
        count = 0
        
        while i < len(r) and r[i]:
            count += 1
            i += 1

        max_1 = max(max_1, count)
    
    return max_1

if __name__ == '__main__':
    n = int(input())

    print(sol(binary_conv(n)))
