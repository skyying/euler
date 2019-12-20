

def is_palindrome(s):
    return str(s) == str(s)[::-1]

def largest_palindrome_product():
    tmp = None
    ans = 0
    for n in range(100, 1000):
        for m in range(100, 1000):
            x = n * m
            if is_palindrome(x) and x > ans:
                ans = x
    return ans


print(largest_palindrome_product())







largest_palindrome_product()

