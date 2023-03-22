import numpy as np

def factor(A, n, pivot):
    """
    a. A is the square matrix of coefficients
    b. n is the rank (number of rows/columns) of A
    c. pivot is an output vector that records the partial pivoting swaps
    """
    pass

def solve(A, n, pivot, b, x):
    """
    a. A, n and pivot are from factor() (A is overwritten with its own LU factorization)
    b. b is a right-hand side to solve for
    c. x is an output vector with the solution of Ax = b
    """
    pass

def readDatFile(fileName):
    numRows = 0
    matrixRows = []
    numRHS = 0
    rightHandSide = []
    with open(fileName, "r") as file:
        numRows = file.readline().strip().split('\n')[0]
        for _ in range(int(numRows)):
            line = file.readline().strip().split(' ')
            matrixRows.append(list(map(int, line)))
        numRHS = file.readline().strip().split('\n')[0]
        for _ in range(int(numRHS)):
            line = file.readline().strip().split(' ')
            rightHandSide.append(list(map(int, line)))

    return matrixRows, rightHandSide


def main():
    """
    Input:
    <rank of system (number of rows)>
    <the rows of the matrix, a>
    <number of right-hand sides>
    <the right hand sides>
    File lu1.dat:
    3
    10 -7 0
    -3 2 6
    5 -1 5
    2
    7 4 6
    3 5 9
    File lu2.dat:
    4
    5 3 -1 0
    2 0 4 1
    -3 3 -3 5
    0 6 -2 3
    2
    11 1 -2 9
    7 7 2 7

    Output
    System Prompt\> prog6 lu1.dat lu2.dat
    File lu1.dat:
    L\\U = 10.00 -7.00 0.00
    0.50 2.50 5.00
    -0.30 -0.04 6.20
    b = 7.00 4.00 6.00
    x = 0.00 -1.00 1.00
    b = 3.00 5.00 9.00
    x = 1.00 1.00 1.00
    File lu2.dat:
    L\\U =5.00 3.00 -1.00 0.00
    0.00 6.00 -2.00 3.00
    0.40 -0.20 4.00 1.60
    -0.60 0.80 -0.50 3.40
    b = 11.00 1.00 -2.00 9.00
    x = 1.00 2.00 -0.00 -1.00
    b = 7.00 7.00 2.00 7.00
    x = 1.00 1.00 1.00 1.00
    """

    lu1MatrixRows, lu1RHS = readDatFile("numerical/lu1.dat")
    print(lu1MatrixRows, lu1RHS)

if __name__ == "__main__":
    main()