#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    _h = s[0:2]
    _m = s[3:5]
    _s = s[6:8]
    _t = s[8:10]

    _h = int(_h)
    if _t == 'AM':
        if _h == 12:
            _h = '00'
        else :
            _h = '0' + _h.__str__()
    else:
        if _h < 12:
            _h = "{}".format(_h+12)

    return "{}:{}:{}".format(_h,_m,_s)
    

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()
    
    result = timeConversion(s)
    f.write(result + '\n')

    f.close()
