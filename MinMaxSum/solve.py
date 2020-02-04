if __name__ == "__main__":
    arr = [1,2,3,4,5]
    arr.sort()
    x = len(arr)-1
    sum1,sum2= 0,0

    for i in range(len(arr)-1):
        sum1 += arr[i]
        sum2 += arr[x-i]
    
    print('{} {}'.format(sum1,sum2))