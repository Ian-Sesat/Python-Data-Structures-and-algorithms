def bubbleSort(A):
	for i in range (0, len(A) - 1):
		done = True
		for j in range (0, len(A) - i - 1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
				done = False
		if done:
			return

ourList=[50,40,80,70,60]
print(ourList)
mySortedList=bubbleSort(ourList)
print(ourList)
		