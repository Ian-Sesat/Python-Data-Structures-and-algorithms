def insertionSort(A):
	for i in range(1, len(A)):
		minNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > minNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = minNum
		
	return A

ourList=[50,40,80,70,60]
mySortedList=insertionSort(ourList)
print(mySortedList)
