
prime_list = {}

def get_nth_prime(n):
    primes = [2, 3, 5, 7]
    p = 11
    while len(primes) < n:
        is_p_prime = True
        for x in primes:
            if p % x == 0:
                is_p_prime = False
                break
        if is_p_prime:
            primes.append(p) 
        p = p + 2
    return primes[len(primes)-1]


print(get_nth_prime(10001))
