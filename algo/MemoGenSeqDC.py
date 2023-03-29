"""
*** At least the following functions need to be in your MemoGenSeqDC.py file ***
    (see lab 2 for detailed instructions on the functions):
        reset, basicOps, genSeqDC, memoGenSeqDC, setS1, setS2

1.  Please copy and paste your <em>entire</em> lab 13.12 solution (D&C genetic sequence alignment) here.
    This implies you can't complete this lab (13.13) until you've successfully completed lab 13.12.
    It also implies you can't complete the analysis of these three algorithms without completing labs 13.11-13.13.

        Prev solution:

        Please implement functions named:  reset, basicOps, genSeqDC, setS1, setS2, and timeComplexity; details follow.
        Please make s1 and s2 global variables, so you don't have to pass them around everywhere

        You don't have to, but you might want to, add a main function and code/test this in your
        favorite Python IDE.

        counter = 0
        s1 = ""
        s2 = ""

        reset, resets basic op counter to 0 and s1/s2 to empty strings
        def reset():
            global counter
            global s1
            global s2
            counter = 0
            s1 = ""
            s2 = ""



            basicOps returns the number of basic operations
            HINT: don't forget to count basic operations!!!

        def basicOps():
            global counter
            return counter

        def setS1(seq):
            global s1
            s1 = seq


            setS2 sets global variable s2 to gene sequence specified

        def setS2(seq):
            global s2
            s2 = seq



            geneSeqDC, implement Genetic Sequence Alignment Algorithm Divide and Conquer Solution.
            Remember: s1 and s2 are global variables.  Therefore, please focus on how i and j affect the optimal
            gene sequence alignment.

            Note the unit tests assume that i and j are zero-based!
            For example given the strings in the slides ("ACGCTGA", "ACTGT"), the unit tests will invoke genSeqDC(len(s1)-1, len(s2)-1)
                or more specifically, for this example, it calculates genSeqDC(6, 4)  *** NOT genSeqDC(7,4) ***

            Please implement it using CS3310Lect9a_GeneSequencing_DP.pdf, which can be found at
                https://uvu.instructure.com/files/104519388/download?download_frd=1.

            However, please implement it using recursion, ***not using an array-cache***

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


        For two gene sequences of size m and n, how many basic operations will the d&c gene-sequencing algorithm perform?
        Please only count the number of function calls.  Please use the lecture 9 algorithm.

        Note: depending on exactly how you implement your divide and conquer algorithm might affect the exact number of basic ops
        This estimate should be the high water mark.  For extra credit, implement the exact number of basic operations that occurs.

        def timeComplexity(m, n):
            s = []
            for i in range(m):
                s.append([])
                for j in range(n):
                    s[i].append(0)

            for i in range(0,m):
                for j in range(0,n):
                    if (i == 0 and j == 0):
                        s[i][j] = 3
                        continue
                    elif (i == 0):
                        s[i][j] = s[i][j-1] + 3
                        continue
                    elif (j == 0):
                        s[i][j] = s[i-1][j] + 3
                        continue

                    d = s[i-1][j-1]
                    h = s[i-1][j]
                    v = s[i][j-1]
                    s[i][j] = d + h + v + 3

            return s[m-1][n-1]
2.  Add clearing of memoization cache to the reset function  (see recommended reset code below)
3.  ***Create a copy***  of the original genSeqDC function (named memoGenSeqDC).  Don't forget in the memoGenSeqDC function
    To modify any genSeqDC calls to be the correct (new) function: memoGenSeqDC.
4.  Add memoization (to cache previously calculated values) in a map called memoizationCache
    in the memoGenSeqDC function.

Hints (the hints are only suggestions; you ***aren't*** required to code your solution this way):
a.  Your code will be much easier to implement and maintain if you also write an helper/intermedite function
    (like getMemoGenSeqDCIfCached).  Refactored code is industry best practice.
    When implemented properly, you will only need to check if the value is cached or not in te helper function.
b.  Test your code by invoking both the original function (genSeqDC) and the new function (memoGenSeqDC) to see
    if you get the same answer.  If not, there's at least one bug in the implementation
c.  If genSeqDC and memoGenSeqDC return the same number of basic operations, there's at least one bug in the implementation,
    because memoization should greatly improve the bottom line!

You need to know how much the cache improves performance for the second analysis assignment (DP vs D&C vs Memoization).
You don't have to, but you might want to, add a main function and code/test this in your favorite Python IDE.
"""
memoizationCache = {}


""" reset, resets basic op counter to 0, s1/s2 to empty strings, and memoizationCache to empty"""
def reset():
    global counter
    global s1
    global s2
    global memoizationCache
    counter = 0
    s1 = ""
    s2 = ""
    memoizationCache = { }

def memoGenSeqDC(i, j):
    pass