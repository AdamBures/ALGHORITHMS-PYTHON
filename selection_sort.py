def selectionSort(arr):
    for i in range(len(arr)):
        minimum = i

        for j in range(i+1,len(arr)):
            if arr[j] < arr[minimum]:
                minimum = j

        arr[minimum],arr[i] = arr[i], arr[minimum]

    return arr

arr = [5,1,3,4,6,7]
print(selectionSort(arr))

