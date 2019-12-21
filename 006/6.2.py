

# This is read from the euler project website after solve the problem

# the formula for sum of each number's square is prove by induction of
# f(n+1) = f(n) + (n+1)^2
# f(n) is a formula menas for any n, we got the sum of 1^2 up to n^2
# f(0) = 0, f(1) = 1. f(2) = 5, f(3) = 14...
# assume  f(n) = an^3 + bn^2 + cn^1 + d and solve the a, b, c, d
# and bring a, b, c, d to this => f(n+1) = f(n) + (n+1)^ 2
# you will get a = 1/3, b = 1/2, c = 1/6, and d = 0
# and use the f(n) to get the sum

def get_sum_square_diff(n):
    return int(((n * (n + 1) / 2) ** 2) - ((2*n+1)*(n+1)*n/6)) 

print(get_sum_square_diff(100))

