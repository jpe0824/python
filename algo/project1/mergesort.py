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

"""
    mergeSort, implement mergeSort
"""
def mergeSort(a):
    global ops_counter
    n = len(a)
    if n > 1:
        m = n // 2
        b = a[:m]
        c = a[m:]
        mergeSort(b)
        mergeSort(c)
        merge(a, b, c)

def merge(a, b, c):
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

