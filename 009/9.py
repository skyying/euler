def find_abc(n):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            c = n - a - b
            if a**2 + b**2 == c ** 2:
                return a*b*c
                

print(find_abc(1000))
