#!/bin/python3

import math
import os
import random
import re
import sys 

def getHourglassSum(m, i, j):
    try:
        return  m[i][j] + m[i][j+1]+ m[i][j+2] +\
                m[i + 1][j+ 1]+\
                m[i+2][j]+ m[i+2][j+1]+m[i+2][j+2]
    except IndexError:
        return -100


if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = -100
    print(result)
    print("--------")

    for i in range(6):
        for j in range(6):
            temp = getHourglassSum(arr,i,j)
            print("{} -> {}".format(6*i + j, temp))
            result = max(
                result,temp)

    print(result)