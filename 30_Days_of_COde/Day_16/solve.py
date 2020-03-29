#!/bin/python3

import sys

def f(n):
    ans = None
    try:
        ans = int(n)
        print(ans)
    except:
        print("Bad String")
    
    return ans

S = input().strip()
f(S)
