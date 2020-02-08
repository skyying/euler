# for 5 * 5
# you can view as following
# the arrow is the direction

# the 1st group has 5 elements, 25, 24, 23, 22, 21
# the 2ed group has 4 elements, 20, 19, 18, 17
# the 3rd group has 4 elements, 16, 15, 14, 13
# the 4th group has 3 elements, 12, 11, 10
# etc ...

#     < < < < < <
# v *5  5  5  5 *5
# v  4 *3  3 *3  3
# v  4  2 *1  1  3
# v  4 *2  2 *2  3
# v *4  4  4  4 *4

# and you can there is a pattern, we only care about the first and last elements in the first group
# and the last element in 2 and 3 group, for the 4th group, we don't care any of their elements
# so we can traverse from back, and sum those elements we care


def spiral(n):
    total = 0
    m = n * n
    els = []
    for i in range(n, 0, -1):
        if i == n:
            els.append(i)
        else:
            els += [i, i]
    for i, e in enumerate(els):
        for x in range(1, e + 1):
            if i % 4 == 0:
                if x == 1 or x == e:
                    total += m
            elif i % 4 == 1 or i % 4 == 2:
                if x == e:
                    total += m
            m -= 1
    return total


print(spiral(1001))
