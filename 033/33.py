import math

# curious fraction is when numerator and denominator have only one common digit
# if that common digit is removed, the resulting fraction is identical
# not trivial => can be mode by 10

def is_curious(n, d):
    n_list = list(str(n))
    d_list = list(str(d))
    intersect = [x for x in n_list if x in d_list]
    if len(intersect) == 0 or len(intersect) > 1:
        return False, 0, 0
    common, = intersect
    has_common = n_list.count(common) == 1 and d_list.count(common) == 1
    n_list.remove(common)
    d_list.remove(common)
    return has_common, int(''.join(n_list)), int(''.join(d_list))


def lowest_term(n, d):
    g = math.gcd(n, d)
    if g == 1:
        return n, d
    while g > 1:
        n //= g
        d //= g
        g = math.gcd(n, d)
    return n, d


def non_trivial_fraction():
    ans_n = 1
    ans_d = 1
    for n in range(11,100):
        for d in range(11, 100):
            if n % 10 == 0 or d % 10 == 0:
                continue
            curious, sn, sd = is_curious(n, d)
            if curious:
                if n/d == sn/sd and sn/sd < 1:
                    ln, ld = lowest_term(sn, sd)
                    ans_n *= ln
                    ans_d *= ld

    an, ad = lowest_term(ans_n, ans_d)
    return ad

print(non_trivial_fraction())
