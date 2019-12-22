
import math
import time


# this algorithm execeeds to 5.06s.
def make_triangle_list(n):
    last = 0;
    cur = 0
    x = 0
    while count_divisor(last) < n:
        x = x + 1
        cur = cur + 1
        last = last + cur

    return last

def count_divisor(n):
    count = 0
    for i in range(1, math.floor(math.sqrt(n)) + 1):
        d1 = n // i
        if d1 * i  == n:
            if d1 != i:
                count += 2
            else:
                count += 1
    return count

# another algorithm uses a table of primes to speed up
