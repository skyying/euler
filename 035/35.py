# get prime under 100

# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes#:~:text=In%20mathematics%2C%20the%20sieve%20of,the%20first%20prime%20number%2C%202.&text=It%20may%20be%20used%20to%20find%20primes%20in%20arithmetic%20progressions.
def get_primes(n):
    is_prime = [False, False] + [True] * (n - 1)
    primes = [2]

    for j in range(4, n + 1, 2):
        is_prime[j] = False

    for i in range(3, n + 1, 2):
        if is_prime[i]:
            primes.append(i)
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return primes, is_prime

def get_all_rotation(n):
    rotations = []
    s = str(n)
    l = len(s)
    for k in range(l):
        rotations.append(int(s[k:] + s[:k]))
    return rotations


def count_circular_primes(n):
    count = 0
    primes, is_prime = get_primes(n)
    for p in primes:
        is_valid = 1
        for r in get_all_rotation(p):
            if not is_prime[r]:
                is_valid = 0
                break
        count += is_valid
    return count

print(count_circular_primes(1000000))


