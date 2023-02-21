# I declare that the following source code was written solely by me.
# I understand that copying any source code, in whole or in part,
# constitutes cheating, and that I will receive a zero on this project
# if I am found in violation of this policy.
import math
ops_counter = 0
"""
    Please implement functions named:  reset, basicOps, quickSort, partition, bestBasicOps, and worstBasicOps; details follow.

    You don't have to, but you might want to, add a main function and code/test this in your
    favorite Python IDE.

"""

""" reset, resets basic op counter to 0 """
def reset():
    global ops_counter
    ops_counter = 0


""" basicOps returns the number of basic operations """
def basicOps():
    return ops_counter


"""
    quickSort, implement quickSort
"""
def quickSort(listToSort, low, high):
    #   parameter a is a list of items to sort in non-decreasing order
    #   low = index into a for beginning of which keys to sort
    #   high = index into a for end of which keys to sort
    #
    #   quickSort algorithm:
    #       terminal condition is when low >= high
    #
    #       otherwise:
    #           pivotPoint = partition(listToSort, low, high pivotPoint)
    #           quickSort(listToSort, low, pivotPoint)
    #           quickSort(listToSort, pivotPoint + 1, high)
    if low < high:
        pivot = partition(listToSort, low, high)
        quickSort(listToSort, low, pivot - 1)
        quickSort(listToSort, pivot + 1, high)


"""
    partition, partitions a[low..high] about pivot (the first element)
    returns partitionIndex (where the line in the sand between lower key <= pivotItem <= highest key
"""
def partition(a, low, high):
    #   parameter a is a list of items of size n, that will be partitioned into
    #   either higher or lower than the pivot
    #
    #   partition:
    #       pivotItem is the item used for key comparisons (a[low])
    #       index of is the index into a, of a next item for key comparisons
    #         (don't forget the +1 for not comparing pivotItem to itself)
    #       pivotIndex is the index into a, of where to swap next item into and out of
    #         to move items less than partition into left side of array (less than pivot)
    #
    #       while (indexOfKey < high)
    #           if (a[indexOfKey] < pivotItem) then
    #               exchange a[indexOfKey] and a[pivotIndex]
    #               // don't want to stomp previous data when moving next item less than pivot
    #               // also, don't want to have pivot index be 0, if there's something below it
    #               // so doing
    #               pivotIndex++
    #           indexOfKey++ // now let's do the same thing for the next key/item
    #
    #
    #  move pivotItem into pivot index, if it isn't already the lowest item
    global ops_counter
    pivotItem = a[low]
    pivotIndex = low
    index = low + 1

    while index <= high:
        ops_counter += 1
        if a[index] < pivotItem:
            a[pivotIndex], a[index] = a[index], a[pivotIndex]
            pivotIndex += 1
        index += 1

    a[pivotIndex], a[low] = a[low], a[pivotIndex]
    return pivotIndex


"""
    bestBasicOps, for a list the size of n, where n is a power of 2 (n = 2^k), this function
    returns b(n), aka the best case or minimal number of key comparisons, as a double

    best case of quick sort only does n - 1 key comparisons but splits the items equally around pivot

    therefore, for bestBasicOps, assume that the recurrence relation is:
        b(1) = 0
        b(n) = 2*b(n/2) + n - 1

    Hint: starting with given b(1), calculate b(2), b(4), etc. until you find a pattern.
    Using the pattern, find a closed form solution.  Then use induction to prove it's true.
    Finally implement here the correct, proven, best-case candidate (closed form) solution.
"""
def bestBasicOps(n):
    # best quickSort == worst mergeSort
    k = math.log2(n)
    return k * (2**k) - (2**k) + 1


"""
    worstBasicOps, for a list the size of n, where n is a power of 2 (n = 2^k), this function
    returns w(n), aka the worst case or maximum number of key comparisons, as a double

    worst case of quick sort does n-1 key comparisons because there's no need to compare the last element to itself

    therefore, for worstBasicOps, assume that the recurrence relation is:
        w(1) = 0
        w(n) = w(n-1) + n - 1

    Hint: starting with given w(1), calculate w(2), w(4), etc. until you find a pattern.
    from this pattern, find a closed form solution.  Then use induction to prove it's true.
    Finally, implement here the correct, proven, worst-case candidate (closed form) solution.

"""
def worstBasicOps(n):
    if n == 1:
        return 0
    return worstBasicOps(n - 1) + n - 1