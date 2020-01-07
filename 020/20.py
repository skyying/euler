
def factorial(n):
    m = 1
    for i in range(1, n+1):
        m *= i
    return str(m)
        

def sum_of_factorial_digits(n):
    m = factorial(n)
    return sum([int(x) for x in m])


print(sum_of_factorial_digits(100))
        
    
