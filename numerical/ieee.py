import math
import numpy as np
import struct
import sys

eps = sys.float_info.epsilon
inf = math.inf

test_pass = 0

def assertEquals(a, b):
    global test_pass
    if a == b:
        print("Pass: ", a)
        test_pass += 1
        return
    print(f"Fail:  expected {b}, but got {a}")

def testIEEE():
    y = 6.5
    subMin = np.nextafter(0,1) #subMin = 5e-324
    assertEquals(sign(y),1) #1
    assertEquals(sign(0.0),0) # 0
    assertEquals(sign(-y),-1) # -1
    assertEquals(sign(-0.0),0) #0
    assertEquals(exponent(y),2) # 2
    assertEquals(exponent(16.6),4) # 4
    assertEquals(fraction(0.0),0.0) #0.0
    assertEquals(mantissa(y),1.625) #1.625
    assertEquals(mantissa(0.0), 0.0) #0.0
    var1 = float('nan')
    assertEquals(exponent(var1),1024) # 1024
    assertEquals(exponent(0.0),0) # 0
    assertEquals(exponent(subMin),-1022) # -1022
    assertEquals(is_posinfinity(math.inf),True) # True
    assertEquals(is_neginfinity(math.inf),False) # False
    assertEquals(not is_posinfinity(-math.inf),True) #True
    assertEquals(is_neginfinity(-math.inf),True) #True
    assertEquals(ulp(y),8.881784197001252e-16) # 8.881784197001252e-16
    assertEquals(ulp(1.0),2.220446049250313e-16) #2.220446049250313e-16
    assertEquals(ulp(0.0),5e-324) #5e-324
    assertEquals(ulp(subMin),5e-324) # 5e-324
    assertEquals(ulp(1.0e15),0.125) # 0.125
    assertEquals(ulps(1,2),4503599627370496) # 4503599627370496

def sign(x):
    # returns -1 if the x is negative, 0 if x is (either positive or negative) zero, 1 if x is positive.
    if x == 0:
        return 0
    if x < 0:
        return -1
    return 1

def exponent(x):
    # returns the unbiased (true) binary exponent of x as a decimal integer. Remember that
    # subnormals are a special case. Consider 0 to be a subnormal.
    if x == 0:
        return 0
    elif math.isnan(x) or math.isinf(x):
        return 1024
    else:
        f = struct.unpack('Q', struct.pack('d', x))[0]
        e = (f >> 52) & 0x7ff
        if e == 0:
            e = -1022
        else:
            e -= 1023
        return e
    # pass

def fraction(x):
    # returns the IEEE fractional part of x as a decimal floating-point number. You must convert
    # binary to decimal. The fraction portion does not include the leading 1 that is not stored.
    f = struct.unpack('Q', struct.pack('d', x))[0]
    fraction = f & 0xfffffffffffff
    fraction /= (1 << 52)
    return fraction

def mantissa(x):
    # returns the full IEEE mantissa of x as a decimal floating-point number (which is the same as
    # fraction() + 1  for normalized numbers; same as fraction() for subnormals).
    if x == 0:
        return fraction(x)
    return fraction(x) + 1

def is_posinfinity(x):
    # returns true if x is positive infinity
    exp = exponent(x)
    man = mantissa(x)
    si = sign(x)
    if exp == 1024 and man == 1.0 and si == 1:
        return True
    return False

def is_neginfinity(x):
    # returns true if x is negative infinity
    exp = exponent(x)
    man = mantissa(x)
    si = sign(x)
    if exp == 1024 and man == 1.0 and si == -1:
        return True
    return False

def ulp(x):
    # returns the magnitude of the spacing between x and its floating-point successor
    y = math.nextafter(x, inf)
    return y - x

def ulps(x, y):
    # returns the number of intervals between x and y by taking advantage of the IEEE standard
    base = 2
    tot_ulps = 0
    exp_y = exponent(y)
    exp_x = exponent(x)
    tmp = exp_x
    while True:
        if tmp < exp_y:
            if tmp == exp_x:
                tot_ulps = ((base ** (exp_x + 1)) - x) / (eps * (base ** exp_x))
            else:
                tot_ulps += (base - 1) * (base ** (64 - 1))
            tmp += 1
        else:
            tot_ulps += (y - (base ** exp_y)) / (eps * (base ** exp_y))
            break
    return tot_ulps

def main():
    testIEEE()
    print(f"\n{test_pass}/22 tests passed")

if __name__ == '__main__':
    main()