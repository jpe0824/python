import numpy as np
import sys

EPS = sys.float_info.epsilon

def golden(func, left, right, tol):
    phi = (1 + np.sqrt(5))/2
    d = (phi - 1) * (right - left)
    x1 = left + d
    x2 = right - d
    f1 = func(x1)
    f2 = func(x2)
    neval = 0
    while abs(right - left) > tol * max(abs(x1), abs(x2)):
        if f1 < f2:
            right = x2
            x2 = x1
            f2 = f1
            d = (phi - 1) * (right - left)
            x1 = left + d
            f1 = func(x1)
        else:
            left = x1
            x1 = x2
            f1 = f2
            d = (phi - 1) * (right - left)
            x2 = right - d
            f2 = func(x2)
        neval += 1
    if f1 < f2:
        xmin = x1
        fmin = f1
    else:
        xmin = x2
        fmin = f2
    return xmin, fmin, neval

def func1(x):
    return ((x**2 / 10) - 2 * (np.sin(x)))

x_min, f_min, num_evals = golden(func1, 0, 4, EPS)
print("Minimum is", f_min, "at x =", x_min)
print("Number of function evaluations:", num_evals)