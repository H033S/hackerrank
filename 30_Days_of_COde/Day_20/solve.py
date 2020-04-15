#!/bin/python3

import sys
def BubbleSort(a):
    swaps_count = 0

    for i in range(len(a)):
        for j in range(len(a)-1):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
                swaps_count += 1
    return (a[0], a[-1], swaps_count)

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

ans = BubbleSort(a)
print("Array is sorted in {} swaps.".format(ans[2]))
print("First Element: " + ans[0].__str__())
print("Last Element: " + ans[1].__str__())