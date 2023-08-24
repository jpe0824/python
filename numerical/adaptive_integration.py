import math

def area(func, a, b, tol=5e-6):
    fa, fb, fc = func(a), func(b), func((a + b) / 2)
    res, nevals = simpson(func, a, b, fa, fb, fc, tol, 3)
    return res, nevals

def simpson(func, a, b, fa, fb, fc, tol, nevals):
    c = (a + b) / 2
    fd = func((c + b) / 2)
    fe = func((a + c) / 2)
    res1 = (b - a) * (fa + 4 * fc + fb) / 6
    res2 = (c - a) * (fa + 4 * fe + fc) / 6
    res3 = (b - c) * (fc + 4 * fd + fb) / 6
    res = res2 + res3

    if abs(res - res1) < tol:
        return res, nevals + 1
    else:
        res1, nevals1 = simpson(func, a, c, fa, fc, fe, tol / 2, nevals)
        res2, nevals2 = simpson(func, c, b, fc, fb, fd, tol / 2, nevals)
        nevals = nevals1 + nevals2
        return res1 + res2, nevals



# Example 1: e^x^2 using a = -1, b = 1
func1 = lambda x: math.exp(x ** 2)
res, nevals = area(func1, -1, 1)
print(f"Estimate for e^x^2 using [-1,1]")
print(f"Integral estimate: {res:.7f}, function evaluations: {nevals}")

# Example 2: sin(x)/x using a = -1, b = 10
func2 = lambda x: math.sin(x) / x if x != 0 else 1
res, nevals = area(func2, -1, 10)
print(f"Estimate for sin(x)/x using [-1,10]")
print(f"Integral estimate: {res:.7f}, function evaluations: {nevals}")

# Example 3: sin(x)/x using a = 0, b = 1
res, nevals = area(func2, 0, 1)
print(f"Estimate for sin(x)/x using [0,1]")
print(f"Integral estimate: {res:.7f}, function evaluations: {nevals}")

