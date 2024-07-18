def quickSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x < pivot]
        right = [x for x in arr[1:] if x >= pivot]
        return quickSort(left) + [pivot] + quickSort(right)
			
ourList=[50,40,80,70,60]
print(ourList)
mySortedList=quickSort(ourList)
print(mySortedList)