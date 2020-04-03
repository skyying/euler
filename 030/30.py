import math


def find_sum(power):
    p = []
    ss = 0
    for i in range(0, 10):
        p.append(int(math.pow(i, power)))

    ps = sum([p[9] for x in range(0, 10)])
    print(ps)
    n = 2
    ts = 0
    ans = []

    while n <= ps:
        a = sum([p[int(x)] for x in list(str(n))])
        if a == n:
            ans.append(a)
        n += 1
    return sum(ans)


print(find_sum(power))
