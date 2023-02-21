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


#     #Reduce the input x to be in [−𝜋/2, 𝜋/2]
#     # Use a Taylor’s Series up to 𝑥21/21! term (you can hard code this in your function or you can write a
#     # findn routine to determine the number of terms that are required),
#     # Handle small angles, i.e., return 𝑥 as sin⁡(𝑥) when 𝑥2 ≤𝜖,
#     # Handle large angles, i.e., return nan when 𝑥 >109
# #Reduce the input x to be in [−𝜋/2, 𝜋/2]
def reduceAngle(x):
    x = x % (2 * math.pi)  # restrict x to be in (-2*pi, 2*pi)
    if x < -math.pi:
        x = x + 2 * math.pi
    elif x > math.pi:
        x = x - 2 * math.pi
    if abs(x) > math.pi / 2:
        x = math.pi - x
    return x

def fact(n):
    s = 1
    for i in range(2, n+1):
        s *= i
    return s

def mySine(x):
    if abs(x) > 1e9:
        return 'nan'
    if abs(x) > math.pi/2:
        return mySine(reduceAngle(x))
    if x < 0:
        return -mySine(-x)
    if x < 1e-8:
        return x
    # # Compute the Taylor series

    n = x
    iterations = 21
    multiplier = 1
    for i in range(3, 3 + iterations, 2):
        multiplier *= -1
        next_term = (x**i) / fact(i) # each term is (x^i) / i!
        n += multiplier * next_term
    return n

def main():
    testSine()
    print(f"\n{test_pass}/9 tests passed")

if __name__ == '__main__':
    main()