
# my solution
# you can check a better algorithm at 6.2.py

def sqrt_of_each(n):
    x = 0
    for i in range(1, n+1):
        x += (i ** 2)
    return x

def get_sum_square_diff(n):
    each = sqrt_of_each(n)
    sum_square = sum([x for x in range(1, n+1)]) ** 2
    return sum_square - each

print(get_sum_square_diff(100))

