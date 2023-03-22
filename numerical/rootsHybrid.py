import math,sys

test_pass = 0

def assertEquals(a, b):
    global test_pass
    if a[0] == b:
        print("Pass: ", a)
        test_pass += 1
        return
    print(f"Fail:  expected {b}, but got {a}")

def testHybrid():
    assertEquals(rootHybrid(func1,2,3), 2.028757838110434)
    assertEquals(rootHybrid(func1,4,5), 4.913180439434884)
    assertEquals(rootHybrid(func2,0.5,1), 0.567143290409784)

def bisect(func, xl, xu, maxit=4):
    if func(xl) * func(xu) > 0:
        return 'does not bracket root'
    for i in range(maxit):
        xm = (xl + xu) / 2
        if func(xm) * func(xl) > 0:
            xl = xm
        else:
            xu = xm
    return xm, xl, xu

def falsePos(func, xl, xu):
    return (xl * func(xu) - xu * func(xl)) / (func(xu) - func(xl))

def check(xl,xu,c,eps):
    return (abs(xl-c) > abs(xl) * eps or abs(xu-c) > abs(xu) * eps)

def rootHybrid(func, xl, xu, eps=sys.float_info.epsilon):
    if func(xl) * func(xu) > 0:
        return 'does not bracket root'
    funcEval = 0
    while True:
        while True:
            funcEval += 1
            c = falsePos(func, xl, xu)
            if func(xl) * func(c) > 0:
                d = falsePos(func,xl,c)
            elif func(xu) * func(c) > 0:
                d = falsePos(func,c,xu)
            xl, xu = sorted([d,c])
            if (abs(d - c) != abs(xu - xl) / 2):
                break
            if xl == xu:
                break
            if not check(xl,xu,c,eps):
                return c, funcEval
        if check(xl,xu,c,eps):
            funcEval += 1
            (c,xl,xu) = bisect(func,xl,xu,maxit=1)
        else:
            return c, funcEval

def func1(x):
    return (x * math.cos(x) + math.sin(x))

def func2(x):
    return (math.e ** (-x) - x)

def main():
    testHybrid()
    print(f"\n{test_pass}/3 tests passed")

if __name__ == "__main__":
    main()