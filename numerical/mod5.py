import math

def bisect(func, xl, xu,maxit = 3):
    if func(xl)*func(xu)>0:
        return 'initial estimates do not bracket solution'
    for i in range(maxit):
        xm = (xl+xu)/2
        if func(xm)*func(xl)>0:
            xl = xm
        else:
            xu = xm
    return xm,xl,xu

def falsePos(func, xl, xu, e = 1.e-15, maxit = 20):

    for i in range(maxit):
        xm = xu - (func (xu) * (xl - xu) / (func (xl) - func (xu)))
        if func(xm) * func(xl) < 0:
            xu = xm
        else:
            xl = xm
    return xm,xl,xu

def func(x):
    return x**2 + 2 * x - 15

def func1(x):
    return (x ** 4 - 3 * x ** 2 + 75 * x - 10000)

def func2(x):
    return 2.7182818284590452353602874713527 ** x - 3 * x

def func3(x):
    return 71991 * ((x * ((1+x)**84))/(((1+x)**84) - 1)) - 1000

def func4(x):
    return x** .5 - math.cos(x)

def main():

    print("Problem 1 ")
    print('Root est, lower guess, upper guess')
    print("bisect: 0, 1",bisect(func4,0,1))
    # print("falsepos: -11, -10",falsePos(func1,-11,-10))

    # print("Problem 2")
    # print('Root est, lower guess, upper guess')
    # print("bisect: 0, 1", bisect(func2,0,1))
    # print("falsePos: 1, 2", falsePos(func2,1,2))

    # print("Problem 3")
    # print(falsePos(func3, 3, 5))
    print(bisect(func, 0,4, 1))

if __name__ == '__main__':
    main()