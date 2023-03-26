import math

"""
    Please implement functions named:  reset, basicOps, genSeqDC, setS1, setS2, and timeComplexity; details follow.
    Please make s1 and s2 global variables, so you don't have to pass them around everywhere

    You don't have to, but you might want to, add a main function and code/test this in your
    favorite Python IDE.
"""
counter = 0
s1 = ""
s2 = ""

""" reset, resets basic op counter to 0 and s1/s2 to empty strings """
def reset():
    global counter
    global s1
    global s2
    counter = 0
    s1 = ""
    s2 = ""


"""
    basicOps returns the number of basic operations
    HINT: don't forget to count basic operations!!!
"""
def basicOps():
    global counter
    return counter

"""
    setS1 sets global variable s1 to gene sequence specified
"""
def setS1(seq):
    global s1
    s1 = seq

"""
    setS2 sets global variable s2 to gene sequence specified
"""
def setS2(seq):
    global s2
    s2 = seq


"""
    geneSeqDC, implement Genetic Sequence Alignment Algorithm Divide and Conquer Solution.
    Remember: s1 and s2 are global variables.  Therefore, please focus on how i and j affect the optimal
    gene sequence alignment.

    Note the unit tests assume that i and j are zero-based!
    For example given the strings in the slides ("ACGCTGA", "ACTGT"), the unit tests will invoke genSeqDC(len(s1)-1, len(s2)-1)
        or more specifically, for this example, it calculates genSeqDC(6, 4)  *** NOT genSeqDC(7,4) ***

    Please implement it using CS3310Lect9a_GeneSequencing_DP.pdf, which can be found at
        https://uvu.instructure.com/files/104519388/download?download_frd=1.

    However, please implement it using recursion, ***not using an array-cache***
"""
def genSeqDC(i, j):
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

"""
For two gene sequences of size m and n, how many basic operations will the d&c gene-sequencing algorithm perform?
Please only count the number of function calls.  Please use the lecture 9 algorithm.

Note: depending on exactly how you implement your divide and conquer algorithm might affect the exact number of basic ops
This estimate should be the high water mark.  For extra credit, implement the exact number of basic operations that occurs.
"""
def timeComplexity(m, n):
    def t(k):
        return (3 ** (k + 1) - 3) // 2

    def r(m, n):
        return t(m * n) ** (1 / (m * n))

    return r(m, n) ** (m * n)