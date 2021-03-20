def double_base_palindromes(n):
    '''
    a number must be odd to be palindromes
    '''
    total = 0
    for i in range(1, n+1, 2):
        base_ten = str(i)
        base_two = format(i, 'b')
        if base_ten == base_ten[::-1] and base_two == base_two[::-1]:
            total += i
    return total


print(double_base_palindromes(1000000))
