import math

test_pass = 0

def assertEquals(a, b):
    global test_pass
    if a == b:
        print("Pass: ", a)
        test_pass += 1
        return
    print(f"Fail:  expected {b}, but got {a}")

def testSine():
    assertEquals(mySine(1.0e-08), 1e-08)
    assertEquals(mySine(0.00001), 9.999999999833334e-06)
    assertEquals(mySine(0), 0)
    assertEquals(mySine(math.pi/2), 1.0000000000000002)
    assertEquals(mySine(math.pi), -0.0)
    assertEquals(mySine(100), -0.5063656411097555)
    assertEquals(mySine(-1000), -0.8268795405320125)
    assertEquals(mySine(999999999), -0.4101372630100049)
    assertEquals(mySine(-1000000001), 'nan')

def mySine(x):
    pass

def main():
    testSine()
    print(f"\n{test_pass}/22 tests passed")

if __name__ == '__main__':
    main()