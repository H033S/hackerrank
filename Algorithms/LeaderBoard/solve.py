def binarySearch(num,arr):
    _min,_max = 0, len(arr)

    while(_min < _max):
        print("{} {}".format(_min, _max))
        med = (_min + _max)//2

        if num < arr[med]:
            _min = med + 1
        elif num >= arr[med]:
            _max = med
        print("{} {}".format(_min, _max))
    



if __name__ == "__main__":
    arr = [8, 7, 6, 4 ,3]
    binarySearch(2,arr)
    print("---------")
    binarySearch(9,arr)
    print("---------")
    binarySearch(5, arr)

