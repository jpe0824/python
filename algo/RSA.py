import numpy as np
from random import randint

"""
    using the Sieve of Eratosthenes, please calculate prime numbers < 2^17
    For this assignment only use prime numbers > 2^16, which is a little less than half the prime numbers)
"""
def sieve():
    global primes, sieves
    sieves = np.zeros(shape=2**17, dtype=np.uint32)
    for i in range(2, len(sieves)):
        if sieves[i] == 0:
            if i > 2**16:
                primes.append(i)
            for j in range(i*i, len(sieves), i):
                sieves[j] = 1


"""
Please see Canvas | Files | Lecture Notes | 'CS3310Lect07-08a_Euclid, Fibonacci, Binet, and Lamé, The first recorded
complexity analysis of an algorithm.' Note: the ***basic*** Euclidean Algorithm only returns the gcd, but your code needs to use
the ***Extended*** Euclidian Algorithm's and return the tuple(gcd, s, and t)

Like the aforementioned document mentions, in section 5.g, the efficiency of the Extended Euclidian algorithm
is big-Theta of (lg n). Since lg n is very efficient, it's okay to calculate the Extended Euclidian Algorithm using D&C (recursively).
However, you can also calculate it iteratively, which has the same time complexity as the D&C does,
but will be an order of magnitude faster than D&C.

The zybook (see see https://learn.zybooks.com/zybook/UVUCS3310Spring2023/chapter/9/section/5)
doesn't do a very good job of clearly defining how to calculate the extended GCD.
Therefore, please see https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm
for the pseudo-code of the Extended Euclidian Algorithm.
"""
def gcd_ex(a, b):
    if a == 0:
        return b, 0, 1
    gcd, s_prev, t_prev = gcd_ex(b % a, a)
    s = t_prev - (b // a) * s_prev
    t = s_prev
    return gcd, s, t


"""
implement modular exponentiation
https://learn.zybooks.com/zybook/UVUCS3310Spring2023/chapter/9/section/7
See Figure 9.7.4: An iterative algorithm for fast modular exponentiation.
"""
def modulo_expo(base, exponent, modulus):
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent = exponent >> 1
        base = (base * base) % modulus
    return result


"""
modulo_number used to calculate d and e will be (p-1)*(q-1)
function should return d, e; function should use extended euclidian algorithm
"""
def get_keys(p, q):
    global primes
    n = p * q
    phi = (p-1) * (q-1)
    e = primes[randint(0,len(primes))]
    gcd, d, _ = gcd_ex(e, phi)
    while d < 0:
        d += phi
    return d, e


"""
c = (m ** e) % n (return c)
where c is the encrypted message (m allowable up to max of a 32 bit unsigned integer, 2^32-1)
"""
def encrypt(m, e, n):
    return modulo_expo(m, e, n)



"""
m = (c ** d) % n (return m)
where m is the decrypted plain text message (up to 32 bit unsigned integer)
"""
def decrypt(c, d, n):
    return modulo_expo(c, d, n)
"""
    Implement RSA Encryption, call your method names, details below:
    sieve(), gcd_ex(a, b), modulo_expo(base, exponent, modulus),
"""

sieves = np.zeros(shape=2**17, dtype=np.uint32)
primes = []
sieve()

# Example usage:
p = primes[-2]  # second largest prime greater than 2^16
q = primes[-3]  # third largest prime greater than 2^16
n = p * q
d, e = get_keys(p, q)
m = 12345
c = encrypt(m, e, n)
m_decrypted = decrypt(c, d, n)
print("Original message: ", m)
print("Encrypted message: ", c)
print("Decrypted message: ", m_decrypted)