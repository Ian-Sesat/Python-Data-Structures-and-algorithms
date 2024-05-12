def linearSearch(arr,target):
    for i in range(len(arr)): # traversing the list
        if arr[i] == target: # comparing the list element with the target value
            return i # return the index if list element is equal to the target element
    return -1 # if target is not present in the list it will return -1

a = [40,50,70,5,8]
print(linearSearch(a,70)) # it will return 2 as 70 is present at 2nd index
print(linearSearch(a,90)) # it will return -1 since 9 is not present in the list