import math

def find_amicable_number(n):
    m = 0
    total = 0
    d = {}
    ans = []
    while m != n:
        m = m + 1 
        if m not in d:
            d[m] = find_division_sum(m)
        
        if d[m] not in d:
            d[d[m]] = find_division_sum(d[m])
            
        if d[d[m]] == m and m != d[m]:
           ans.append(m)
    return sum(ans)
        

def find_division_sum(m):
    tmp_m = m
    div = [1]
    for i in range(2, math.floor(math.sqrt(m))):
        if m % i == 0:
            div = div + [i, math.floor(m / i)]
    return sum(div)


print(find_amicable_number(10000))


