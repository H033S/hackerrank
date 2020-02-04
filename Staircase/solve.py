
if __name__ == "__main__":
    
    n = int(input("dasd\n"))
    count = n 
    ar = ['' for x in range(n)]
    

    for i in range(n-1,-1,-1):
        for j in range(0,n-count):
            ar[i] += ' '
        for j in range(count):
            ar[i] += '#'
        count -= 1    

    for x in ar:
        print(x)