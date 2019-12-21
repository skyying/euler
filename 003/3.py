import math

## Solution
# 做法，把這個數字除以第一個 `prime number`, 一直到無法整除，接下來除以第二個 `prime number...` 一次類推，一直到最後剩下的數字也是 `prime number` 爲止, 要考慮到不要一直重複的檢查某個數字是否爲prime, 只要有檢查過，就記下來。這樣之後再使用就可用O(1) 的時間來判斷是否是 `prime`


prime_list = {}

def is_prime(n):
    primes = [2, 3, 5, 7]

    if n in prime_list:
        return True

    for p in primes:
        if p == n:
            prime_list[p] = True
            return True
        if n % p == 0:
            return False

    sr = int(math.sqrt(n)) + 1

    for i in range(2, sr):
        if n % i == 0:
            return False

    prime_list[n] = True

    return True


def prime_factor(n):
    m = n
    primes = []
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
                    return max(primes)

                if is_prime(m):
                    primes.append(m)
                    break

            if cur_prime != None:
                primes.append(cur_prime)
                cur_prime = None

    return max(primes)

print(prime_factor(600851475143))

