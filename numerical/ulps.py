import sys
import math
base = sys.float_info.radix
eps = sys.float_info.epsilon
prec = sys.float_info.mant_dig
inf = math.inf
test_pass = 0

def assertEquals(a, b):
    global test_pass
    if a == b:
        print("Pass: ", a)
        test_pass += 1
        return
    print(f"Fail:  expected {b}, but got {a}")

def testUlps():
    assertEquals(ulps(-1.0, -1.0000000000000003), 1)
    assertEquals(ulps(1.0, 1.0000000000000003), 1)
    assertEquals(ulps(1.0, 1.0000000000000004), 2)
    assertEquals(ulps(1.0, 1.0000000000000005), 2)
    assertEquals(ulps(1.0, 1.0000000000000006), 3)
    assertEquals(ulps(0.9999999999999999, 1.0), 1)
    assertEquals(ulps(0.4999999999999995, 2.0), 9007199254741001)
    assertEquals(ulps(0.5000000000000005, 2.0), 9007199254740987)
    assertEquals(ulps(0.5, 2.0), 9007199254740992)
    assertEquals(ulps(1.0, 2.0), 4503599627370496)
    assertEquals(2.0**52, 4503599627370496.0)
    assertEquals(ulps(-1.0, 1.0), inf)
    assertEquals(ulps(-1.0, 0.0), inf)
    assertEquals(ulps(0.0, 1.0), inf)
    assertEquals(ulps(5.0, math.inf), inf)
    assertEquals(ulps(15.0, 100.0), 12103423998558208)

def ulps(x, y):
    if (x == inf or y == inf) \
            or (x == 0 or y == 0) \
            or ((x > 0) and (y < 0)) \
            or ((x < 0) and (y > 0)):
        return inf
    x = abs(x)
    y = abs(y)
    exp_x, exp_y, lub, glb = 0, 0, 1, 1

    if x > y:
        x, y = y, x

    while lub <= x:
        lub *= base
        exp_x += 1
    while lub > x:
        lub /= base
        exp_x -= 1

    while glb <= y:
        glb *= base
        exp_y += 1
    while glb > y:
        glb /= base
        exp_y -= 1

    tot_ulps = 0
    tmp = exp_x
    while True:
        if tmp < exp_y:
            if tmp == exp_x:
                tot_ulps = ((base ** (exp_x + 1)) - x) / (eps * (base ** exp_x))
            else:
                tot_ulps += (base - 1) * (base ** (prec - 1))
            tmp += 1
        else:
            tot_ulps += (y - (base ** exp_y)) / (eps * (base ** exp_y))
            break
    return tot_ulps

def main():
    testUlps()
    print(f"\n{test_pass}/16 tests passed")

if __name__ == '__main__':
    main()