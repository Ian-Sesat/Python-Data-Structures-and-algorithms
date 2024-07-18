def quicksort(arr, lo, hi):
    if lo < hi:
        # Partition the array and get the pivot index
        p = partition(arr, lo, hi)
        # Recursively apply QuickSort to the left of the pivot
        quicksort(arr, lo, p - 1)
        # Recursively apply QuickSort to the right of the pivot
        quicksort(arr, p + 1, hi)

def partition(arr, lo, hi):
    # Choose the pivot as the last element
    pivot = arr[hi]
    # Temporary pivot index
    i = lo
    for j in range(lo, hi):
        if arr[j] < pivot:
            # Swap arr[i] and arr[j]
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    # Place the pivot in its correct position
    arr[i], arr[hi] = arr[hi], arr[i]
    return i

# Example usage

tests = [
        [11,9,29,7,2,15,28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6]
    ]

for elements in tests:
        quicksort(elements, 0, len(elements)-1)
        print(f'sorted array: {elements}')