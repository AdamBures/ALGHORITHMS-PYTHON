def binarySearch(arr,l,r,x):
    while l <= r:
        mid = l+(r-l)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            l = mid+1
        else:
            r=mid-1
    return -1

arr = [5,1,3,4,6]
x = int(input())
result = binarySearch(arr,0,len(arr)-1,x)
if result != -1:
    print(f"Element is present at {result}")

else:
    print("Element is not present")
