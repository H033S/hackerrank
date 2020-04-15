from math import sqrt

def isPrime(n):
    if n == 1:
        return False
        
    for x in range(2,int(sqrt(n))+1):
        if n % x == 0:
            return False
    return True

n = int(input())

for i in range(n):
    print("{}".format("Prime" if isPrime(int(input())) else "Not prime"))
