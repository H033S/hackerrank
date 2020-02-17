import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr.sort()

    _min = sum(arr[:-1])
    _max = sum(arr[1:])

    print('{} {}'.format(_min,_max))


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
