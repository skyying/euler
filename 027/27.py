from collections import defaultdict
primes = defaultdict(lambda: None)
import time


def start():
    p = [2, 3, 5, 7]
    for x in p:
        primes[x] = True


def is_prime(n):
    if n == 0:
        return False
    if n in primes:
        return True
    for p in primes:
        if n % p == 0:
            return False
    for i in range(9, n, 2):
        if n % i == 0:
            return False
    primes[n] = True
    return True


# brute force
# this takes up to 5s
def quadratic_primes():
    start()
    ma = None
    mb = None
    mn = 0
    for a in range(-999, 1001):
        for b in range(-999, 1001):
            n = 0
            while is_prime(abs((n * n) + (a * n) + b)):
                n += 1
            if n > mn:
                ma = a
                mb = b
                mn = n
    return ma * mb


s = time.time()
print(quadratic_primes())
print(time.time() - s)
