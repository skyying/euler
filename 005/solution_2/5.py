import math

# the idea is the same, find all possible factors for 2-K, K=20,
# but the prime factorisation for each number is too waste time
# we should find a way to determine the exponent for each factor

# for each prime, if p ^ (a - 1) > 20, we know the maxium exponent 
# for this prime

def is_prime(n):
    primes = [2, 3, 5, 7]
    if n in primes:
        return True
    for p in primes:
        if n % p == 0:
            return False
        if n == p:
            return True
    for i in range(9, n, 2):
        if n % i == 0:
            return False
    return True


def get_primes(n):
    primes = []
    for i in range(2, n+1):
        if is_prime(i):
            primes.append(i)
    return primes


def prime_and_exponent(n, p):
    return (p, math.floor(math.log(n, p)))

def get_smallest_multiple(n):
    prime_list = get_primes(n)
    primes = [x[0] ** x[1] for x in [prime_and_exponent(n, p) for p in prime_list]]
    multiple = 1
    for p in primes:
        multiple *= p 
    return multiple
    
print(get_smallest_multiple(20))


