counter = 0
s1 = ""
s2 = ""
memoizationCache = { }

def reset():
    """
    resets a global op counter, as well as two global strings s1 and s2
    (which will contain gene sequences); also resets the global memoizationCache
    """
    global counter
    global s1
    global s2
    counter = 0
    s1 = ""
    s2 = ""

def basicOps():
    """
    returns the value of the global op counter
    """
    global counter
    return counter

def setS1(seq):
    """
    associates the global s1 with the string in seq
    """
    global s1
    s1 = seq

def setS2(seq):
    """
    associates the global s2 with the string in seq
    """
    global s2
    s2 = seq

def genSeqDC(i, j):
    """
    your D&C gene sequence alignment function from the previous assignment.
    Recursively performs alignment of the 0 through i and 0 through j characters of the strings s1 and s2.
    """
    global s1
    global s2
    global counter
    # Note the unit tests assume that i and j are zero-based!
    # For example given the strings in the slides ("ACGCTGA", "ACTGT"), the unit tests invoke genSeqDC(len(s1)-1, len(s2)-1)
    # or more specifically, for this example, it calculates genSeqDC(6, 4)  *** NOT genSeqDC(7,4) ***
    counter += 1

    if i < 0 and j < 0:
        return 0
    if i < 0:
        return (j + 1) * 5
    if j < 0:
        return (i + 1) * 5

    indel = 5
    match = -3
    subst = 1
    dist = match if s1[i] == s2[j] else subst

    cost1 = genSeqDC(i-1, j-1) + dist
    cost2 = genSeqDC(i-1, j) + indel
    cost3 = genSeqDC(i, j-1) + indel

    return min(cost1, cost2, cost3)

def memoGenSeqDC(i, j):
    """
    Recursively performs alignment of the 0 through i and 0 through j characters of the strings s1 and s2;
    using memoization to avoid redundant recursive calls.
    """
    global memoizationCache
    global counter
    counter += 1

    if i < 0 and j < 0:
        return 0
    if i < 0:
        return (j + 1) * 5
    if j < 0:
        return (i + 1) * 5

    if (i, j) in memoizationCache:
        return memoizationCache[(i, j)]

    indel = 5
    match = -3
    subst = 1
    dist = match if s1[i] == s2[j] else subst

    cost1 = memoGenSeqDC(i-1, j-1) + dist
    cost2 = memoGenSeqDC(i-1, j) + indel
    cost3 = memoGenSeqDC(i, j-1) + indel

    result = min(cost1, cost2, cost3)
    memoizationCache[(i, j)] = result
    return result