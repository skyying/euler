from operator import mul
from functools import reduce
import numpy as np

# this is a very good practice for matrix looping

def read_file():
    fp = open('./in', 'r')
    content = []
    for line in iter(fp):
        line = line.strip("\n")
        content.append([int(x)  for x in line.split(" ")])
    fp.close()
    return content

def draw(ary):
    [print("".join(str(x))) for x in ary]


def greatest_product(grid):
    return max([vertical_horizon(grid), diagonal(grid)])
    

def vertical_horizon(grid):
    r = len(grid)
    c = len(grid[0])
    ans = 0
    interval = 4
    # left and right
    for i in range(0, r):
        for j in range(0, c-interval - 1):
            product = reduce(mul, grid[i][j:j+interval], 1)
            if ans < product:
                 ans = product
    # up and down
    vv = np.array(grid)
    for i in range(0, c):
        vertical_line = vv[:, i]
        for j in range(0, len(vertical_line)-interval - 1):
            product = reduce(mul, vertical_line[j: j+interval], 1)
            if ans < product:
                ans = product
    return ans


def diagonal(grid):
    r = len(grid)
    c = len(grid[0])
    ans = 0
    for i in range(0, r-3):
        # direction \
        for j in range(0, c-3):
            line = [grid[i+x][j+x] for x in range(0,4)]
            print(line)
            product = reduce(mul, line, 1)
            if ans < product:
                ans = product
        # direction / 
        for k in range(c-1, 2, -1):
            line = [grid[i+x][k-x]  for x in range(0, 4)]
            product = reduce(mul, line, 1)
            if ans < product:
                ans = product
    return ans

f = read_file()
print(greatest_product(f))

