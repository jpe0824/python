import math

ops_counter = 0

""" reset, resets basic op counter to 0 """
def reset():
    global ops_counter
    ops_counter = 0

"""
    basicOps returns the number of basic operations
    HINT: don't forget to count basic operations!!!
"""
def basicOps():
    return ops_counter

def partition(array, low, high):
    global ops_counter
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        ops_counter += 1
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])

    (array[i + 1], array[high]) = (array[high], array[i + 1])

    return i + 1

def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)

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