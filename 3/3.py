import math
def prime_factor(n):
    print(n)

list = {}

def is_prime(n):
    if n in list:
        return True
    if n == 2 or n == 3 or n == 5:
        list[n] = True
        return True
    if n % 2 == 0 or n % 3 == 0 or n % 5 == 0:
        return False
    if n < 9:
        list[n] = True
        return True
    i = 2
    sr = math.sqrt(n)
    while i < int(sr):
        if n % i == 0:
            return False
        i += 1
    list[n] = True
    return True

        


def prime_factor(n):
    m = n
    prime = []
    
    for i in range(2, n + 1):
        if is_prime(i):
            cur_prime = None
            while (m % i) == 0 and ((m / float(i)) % 1 == 0):
                cur_prime = i
                t = m / i
                
                if t % 1 != 0:
                    break
                else:
                    m = int(t)

                if m == 1:
                    return max(prime)

                if is_prime(m):
                    prime.append(m)
                    break

            if cur_prime != None:
                prime.append(cur_prime)
                cur_prime = None
    return max(prime)
    
print(prime_factor(600851475143))
