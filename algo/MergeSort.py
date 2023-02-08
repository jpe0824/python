import math

"""
    Please implement functions named:  reset, basicOps, mergeSort, merge, bestBasicOps, and worstBasicOps; details follow.

    You don't have to, but you might want to, add a main function and code/test this in your
    favorite Python IDE.
"""

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

"""
    mergeSort, implement mergeSort
"""
def mergeSort(a):
    #   parameter a is a list of items to sort in non-decreasing order
    #
    #   mergeSort (a Divide and Conquer) algorithm:
    #       terminal condition is when len(items), aka n, is 1.  A list of 1 item is properly sorted!
    #
    #       otherwise:
    #           m (middle element)  equals the floor of n/2, hint the integer division operator in Python is //
    #           copy first m elements, items[0..m-1] from items into a new list b[0..m-1]
    #           copy remaining elements from items[m..n-1] into a new list c[0..n-1-m]
    #           mergeSort(b)
    #           mergeSort(c)
    #           merge(a, b, c)
    global ops_counter
    n = len(a)
    if n > 1:
        m = n // 2
        b = a[:m]
        c = a[m:]
        mergeSort(b)
        mergeSort(c)
        merge(a, b, c)

"""
    merge, merges the sorted lists b and c into a.
"""
def merge(a, b, c):
    # parameter a is a list of items of size n, where n = len(b) + len(c), that will contain
    #       sorted items from b and c in non-decreasing order
    #   parameter b is first half of list a sorted in non-decreasing order
    #   parameter c is second half of list a sorted in non-decreasing order
    #
    #   merge:
    #       n (length of a)
    #       m (middle element) equals the floor of n/2, hint the integer division operator in Python is //
    #       i is the current index of a (where to insert next sorted item), initially i == 0
    #       j is the current index of b (where to get value used for key comparison), initially j == 0
    #       k is the current index of c (where to get value used for key comparison), initially k == 0
    #
    #       // assign smaller of next item in b or next item in c into the next item in a
    #       while j < m and k < n - m
    #           if (b[j] <= c[k]) then
    #               a[i] = b[j]
    #               j++
    #           else
    #               a[i] = c[k]
    #               k++
    #           i++
    #
    #       // If any values remain in b or c, implies that the remaining items
    #       // are larger than the last item inserted into the merged list (a).
    #       // Therefore, append any remaining items
    #       // also, exactly one case is true, since we don't compare the last item to itself either
    #       if (j < m) then
    #           copy b[j..m-1] into a[i..n-1]
    #       else if (k < n - m) then
    #           copy c[k..n-m-1] into a[i..n-1]
    global ops_counter
    i = j = k = 0
    n = len(b) + len(c)
    m = len(b)
    while j < m and k < n - m:
        if b[j] <= c[k]:
            a[i] = b[j]
            j += 1
        else:
            a[i] = c[k]
            k += 1
        i += 1
        ops_counter += 1
    if j < m:
        a[i:n] = b[j:m]
    else:
        a[i:n] = c[k:n - m]

"""
    bestBasicOps, for a list the size of n, where n is a power of 2 (n = 2^k), this function
    returns b(n), aka the best case or minimal number of key comparisons, as a double

    best case of merge sort only does n/2 key comparisons because either b[m-1] < c[0] or b[0] < c[n-1-m]

    therefore, for bestBasicOps, assume that the recurrence relation is:
        b(1) = 0
        for n>1, n a power of 2 is:  b(n) = 2*b(n/2) + n/2

    Hint: starting with given b(1), calculate b(2), b(4), etc. until you find a pattern.
    Using the pattern, find a closed form solution.  Then use induction to prove it's true
    implement here the candidate solution
"""
def bestBasicOps(n):
    return (math.log2(n/2) + 1) * n/2


"""
    worstBasicOps, for a list the size of n, where n is a power of 2 (n = 2^k), this function
    returns w(n), aka the worst case or maximum number of key comparisons, as a double

    worst case of merge sort does n-1 key comparisons because there's no need to compare the last element to itself

    therefore, for worstBasicOps, assume that the recurrence relation is:
        w(1) = 0
        for n>1, n a power of 2 is:  w(n) = 2*w(n/2) + n - 1

    Hint: starting with given w(1), calculate w(2), w(4), etc. until you find a pattern
    from this pattern, find a closed form solution.  Then use induction to prove it's true
    implement here the candidate solution

"""
def worstBasicOps(n):
    k = math.log2(n)
    return k * (2**k) - (2**k) + 1

