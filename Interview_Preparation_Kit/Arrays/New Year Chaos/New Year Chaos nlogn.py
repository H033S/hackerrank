def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        l_bribes = mergeSort(L)
        r_bribes = mergeSort(R)


        bribes = 0
        i , j , k = 0 , 0 , 0 
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else :
                bribes += len(L) - i
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            k += 1
            j += 1

        return bribes + l_bribes + r_bribes
    
    else: 
        return 0

def minimumBribes(q):
    for i, P in enumerate(q):
        P -= 1

        if P - i < 3:
            continue
        
        print('Too chaotic')
        return
    print(mergeSort(q))

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
