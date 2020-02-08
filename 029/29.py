# ab for 2 ≤ a ≤ 100 and 2 ≤ b ≤ 100?


def distinct_powers(n):
    d = {}
    total = 0
    for a in range(2, n + 1):
        for b in range(2, n + 1):
            result = a**b
            if result not in d:
                total += 1
                d[result] = 1
    return total


print(distinct_powers(100))
