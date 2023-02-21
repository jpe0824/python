import sys
import numpy as np

MAX_ITER = 100_000

EPS = sys.float_info.epsilon

def regFalsiResult(xLower, xUpper, func):
    print('Results for: ',func.__name__)
    root, flag, fxRoot, iteration = regFalsi(xLower, xUpper, func)
    if flag == -1:
        print('No root found.')
        return
    if flag == 1:
        print('Max iterations reached')
        return
    print('Root found: ', root)
    print('Function val at root: ', fxRoot)
    print('No. of iterations: ', iteration)

def regFalsi(xLower, xUpper, func):
    if func(xLower) * func(xUpper) < 0:
        return None, -1, None, None
    if func(xLower) == 0:
        return xLower, 0, 0, 0
    if func(xUpper) == 0:
        return xUpper, 0, 0, 0
    root = xLower
    iteration = 0
    while iteration < MAX_ITER:
        prevRoot = root
        root = (xLower * func(xUpper) - xUpper * func(xLower)) / (func(xUpper) - func(xLower))

        if func(root) < EPS:
            break
        if func(root) == 0:
            break
        if np.isclose(root, prevRoot, rtol = 0, atol=EPS):
            break
        elif func(root) * func(xLower) < 0:
            xUpper = root
        else:
            xLower = root
        iteration += 1

    if iteration == MAX_ITER:
        return None, 1, None, iteration
    return root, 0, func(root), iteration
    # Calculate a new approximated root using the formula of regula falsi in a loop.
    # Break out the loop and return the proper values if one of the following conditions is
# met:
# The func(root)< (machine epsilon)
# The distance between approximated roots in two consecutive iteration is less a
# ulp apart at the root location
# The loop reached the maximum number of iterations. Set maxInt to 100000 in
# your program.

def func1(x):
    return (x ** 4) - (6 * x ** 3) + (12 * x ** 2) - (10 * x) + 3

def func2(x):
    return (x ** 3) - (7 * x ** 2) + (15 * x) - 9

def main():
    lower1, lower2 = 1.5, 0
    upper1, upper2 = 2.5, 1.5
    regFalsiResult(lower1, upper1, func1)
    regFalsiResult(lower2, upper2, func1)
    regFalsiResult(lower1, upper1, func2)
    regFalsiResult(lower2, upper2, func2)

if __name__ == '__main__':
    main()