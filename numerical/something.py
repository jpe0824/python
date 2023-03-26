def f(x):

    return x**4-7*x**2-6*x

x1 = 1
x2 = 2
x3 = 3

top = ((x2 - x1) ** 2) * (f(x2) - f(x3)) - ((x2-x3) ** 2) * (f(x2) - f(x1))
bottom = ((x2 - x1) * (f(x2) - f(x3)) - (x2 - x3) * (f(x2) - f(x1)))

x4 = x2 - (0.5* (top/bottom))

print(x4)