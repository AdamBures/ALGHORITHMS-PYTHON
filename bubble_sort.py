def bubbleSort(arr):
    def swap(i,j):
        arr[i],arr[j] = arr[j], arr[i]

    n = len(arr)
    swapped = True

    x = -1
    while swapped:
        swapped = False
        x += 1
        for i in range(1,n-x):
            if arr[i-1] > arr[i]:
                swap(i-1,i)
                swapped = True

    return arr

arr = [5,1,3,4,6,7]
print(bubbleSort(arr))
