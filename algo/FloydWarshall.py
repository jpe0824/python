"""
    Please implement functions named:  reset, basicOps, floyd, timeComplexity, spaceComplexity; details follow.

    You don't have to, but you might want to, add a main function and code/test this in your
    favorite Python IDE.
"""
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
    floyd, implement Floyd Warshall Algorithm
    d = distance matrix.  When the function is invoked, it will be the cost of the various edges (D|(0))
        note: if the distance is infinity, then the distance in the matrix will be Inf,
              so any connected vertices inserted that creates a path will be shorter than inf.
              Of course you may just check for inf with math.isinf(item) if you want or use it as if it's a
              'real' floating point value
        therefore, check for infinity by checking math.isnan(intValue)
    p = path matrix.  When the function is invoked, p will be filled with zeros.
        p will also be the same size as d
    both p and d will be n*n matrix (where n is the number of vertices)
"""
def floyd(d, p):
    # initialize paths
    # k is the outer most loop.  we are checking if we insert node k in between Edge(i, j) is it shorter?
    # for(k = 0; k < n; i++) {
    #     // Now check for all possible edge combinations (i, j), since it is a directed graph
    #     for(i = 0; i < n; i++) {
    #         for (j = 0; j < n; j++) {
    #             // if inserting k between i, j is shorter, then update it to use the shorter path
    #             if (d[i][k] + d[k][j] < d[i][j]) then {
    #                  d[i][j] = d[i][k] + d[k][j];
    #                  p[i][j] = k + 1
    #             }
    #         }
    #     }
    # }
    global ops_counter
    n = len(d)

    for i in range(n):
        for j in range(n):
            p[i][j] = 0

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if not math.isinf(d[i][k]) and not math.isinf(d[k][j]) and d[i][k] + d[k][j] < d[i][j]:
                    ops_counter += 1
                    d[i][j] = d[i][k] + d[k][j]
                    p[i][j] = k + 1

"""
    For a directed graph with n-nodes, how many basic operations will Floyd-Warshall perform?
"""
def timeComplexity(n):
    return n**3

"""
    For a directed graph with n-nodes, how much memory will Floyd-Warshall require
    to calculate the all path's shortest distances?
"""
def spaceComplexity(n):
    return n**2