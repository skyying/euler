import math

# using sieve of eratosthenes
# this is much faster, the execution time is about 0.482s.
# the concept of this algorithm can be found in this video
# https://www.youtube.com/watch?v=eKp56OLhoQs


# find sum of prime below n
def sum_of_primes(n):
    primes = [1 for i in range(0, n + 1)]
    # mark 0 and 1 as not primes
    primes[0] = 0
    primes[1] = 0

    # assume p is next number that have not been crossed out,
    # we only need to start crossing out at p^2
    # because any smaller multiple of p has a prime divisor less than p
    # has been crossed out as a multple of that, this is also the reason why
    # we only stop after we reached math.sqrt(n)
    limit = math.ceil(math.sqrt(n)) 

    for i in range(2 , limit):
        if primes[i] == 1:
            for j in range(i * i, n+1, i):
                primes[j] = 0

    return sum([ i if x == 1 else x for i, x in enumerate(primes)])

print(sum_of_primes(2000000))
