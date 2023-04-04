basic_op_count = 0


def reset():
    """Resets basic operation counter to 0"""
    global basic_op_count
    basic_op_count = 0


def basicOps():
    """Returns the number of basic operations"""
    global basic_op_count
    return basic_op_count


def geneSeqDP(s1, s2):
    """
    Implements Genetic Sequence Alignment algorithm Dynamic Programming Solution.
    Uses Needleman/Wunsch constants:
        penalty for match is -3
        penalty for subst is 1
        penalty for indel is 5
    """
    global basic_op_count
    m = len(s1)
    n = len(s2)

    # allocate and initialize the 2D array S
    S = [[0] * (n+1) for i in range(m+1)]
    indel = 5
    match = -3
    subst = 1

    for i in range(1, m+1):
        S[i][0] = i * indel
    for j in range(1, n+1):
        S[0][j] = j * indel

    for i in range(1, m+1):
        for j in range(1, n+1):
            basic_op_count += 1
            dist = match if s1[i-1] == s2[j-1] else subst
            S[i][j] = min(
                S[i-1][j-1] + dist,
                S[i-1][j] + indel,
                S[i][j-1] + indel
            )

    return S[m][n]


def timeComplexity(m, n):
    """
    Returns an approximation of the number of basic operations the gene-sequencing algorithm will perform.
    """
    return (m * n) + m + n


def spaceComplexity(m, n):
    """
    Returns an approximation of the additional memory the gene-sequencing algorithm will use.
    """
    return (m+1) * (n+1)
