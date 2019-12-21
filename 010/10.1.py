import math

# this algorithm execution time execeeds 4.735 seconds
# check a better algorithm in 10.2.py

def is_prime(n):
    if n == 1:
        return False
    if n < 4:
        return True
    if n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    r = math.floor(math.sqrt(n))
    f = 5
    while f <= r:
        if n % f == 0 or n % (f+2) == 0:
            return False
        f = f+6
    return True

def sum_of_prime(n):
    ans = 2
    primes = [2]
    for i in range(3, n, 2):
        if is_prime(i):
            ans += i
            primes.append(i)
    return ans

print(sum_of_prime(2000000))


