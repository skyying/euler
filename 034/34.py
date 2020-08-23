
fac = {0: 1}

def prepare_boundary():
    f = 1
    for i in range(1, 10):
        f *= i
        fac[i] = f

    boundary = 0
    for val in fac.values():
        boundary += val
    return boundary


def sum_of_curious():
    upper_bound = prepare_boundary()
    total = 0
    for i in range(10, upper_bound):
        result = sum([fac[int(n)] for n in list(str(i))])
        if result == i:
            total += i
    return total

print(sum_of_curious())
