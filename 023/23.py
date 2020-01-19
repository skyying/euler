import math

# this takes about 2 and half seconds to run


def sum_of_divisors(n):
    if n == 1:
        return 1
    root = math.ceil(math.sqrt(n))
    divisors = []
    for i in range(2, root):
        if n % i == 0:
            divisors += [i, n // i]
    if root**2 == n:
        divisors.append(root)
    return sum(divisors) + 1


def calc_non_abundant_sums(n):
    made_by_two_abundants = {}
    all_pos_sum_up_to_n = n * (n + 1) // 2
    abundants = []

    for i in range(1, n + 1):
        if i < sum_of_divisors(i):
            abundants.append(i)
            for x in abundants:
                if x + i <= n:
                    made_by_two_abundants[x + i] = 1
        if i in made_by_two_abundants:
            all_pos_sum_up_to_n -= i
    return all_pos_sum_up_to_n


print(calc_non_abundant_sums(28123))
