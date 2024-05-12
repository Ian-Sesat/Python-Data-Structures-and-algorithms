def binarySearch(arr,target):
    l = len(arr) - 1
    start,end = 0,l 
    mid = (start+end)//2 
    while start <= end:
        if arr[mid] == target: 
            return mid 
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
        mid = (start+end)//2
    return -1
    
a = [1,2,4,5,8]
print(binarySearch(a,5)) # it will return 3 as 5 is present at 3rd index
print(binarySearch(a,9)) # it will return -1 since 9 is not present in the list