import math
import random
import time

def mergeSort(a):
    global comps, swaps
    n = len(a)
    if n > 1:
        m = n // 2
        b = a[:m]
        c = a[m:]
        mergeSort(b)
        mergeSort(c)
        i = j = k = 0
        while j < m and k < n - m:
            comps += 1
            if b[j] <= c[k]:
                a[i] = b[j]
                j += 1
            else:
                a[i] = c[k]
                k += 1
            swaps += 1
            i += 1
        if j < m:
            a[i:n] = b[j:m]
            swaps += m - j
        else:
            a[i:n] = c[k:n - m]
            swaps += n - m - k

def quickSortIterative(arr, low, high):
    # Create an empty stack
    stack = []

    # Push initial values of low and high to stack
    stack.append((low, high))

    # Loop until stack is empty
    while stack:

        # Pop top pair from stack and get sub-array
        low, high = stack.pop()
        pivot = partition(arr, low, high)

        # If there are elements on left side of pivot,
        # push sub-array to stack
        if pivot - 1 > low:
            stack.append((low, pivot - 1))

        # If there are elements on right side of pivot,
        # push sub-array to stack
        if pivot + 1 < high:
            stack.append((pivot + 1, high))

def partition(a, low, high):
    pivot = a[high]
    i = low - 1
    for j in range(low, high):
        if a[j] < pivot:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i+1], a[high] = a[high], a[i+1]
    return i + 1


sizes = [2**k for k in range(10,21)]

for size in sizes:
    data = [random.randint(-1000, 1000) for _ in range(size)]
    comps, swaps = 0, 0
    start = time.time()
    mergeSort(data)
    end = time.time()
    merge_time = end - start
    merge_comps, merge_swaps = comps, swaps
    comps, swaps = 0, 0
    start = time.time()
    quickSortIterative(data, 0, size - 1)
    end = time.time()
    quick_time = end - start
    quick_comps, quick_swaps = comps, swaps
    print(f"Size {size}: Merge Sort Time = {merge_time:.6f} sec, "
        f"Merge Sort Comps = {merge_comps}, Merge Sort Swaps = {merge_swaps}, "
        f"Quick Sort Time = {quick_time:.6f} sec, Quick Sort Comps = {quick_comps}, "
        f"Quick Sort Swaps = {quick_swaps}")
