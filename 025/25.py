def find_fib(n):
    prev = 1
    cur = 2
    count = 3
    while len(str(cur)) < n:
        tmp = prev
        prev = cur
        cur = tmp + cur
        count += 1
    return count


print(find_fib(1000))
