
# Lattice_path
# https://en.wikipedia.org/wiki/Lattice_path

def create_grid(r, c):
    return [[0 for x in range(c)] for y in range(r)]

def paint_grid(grid):
    return [print(",".join([str(x) for x in y ])) for y in grid]

def calc_paths(grid):
    for r in range(0, len(grid)):
        for c in range(0, len(grid[0])):
            if r == 0 or c == 0:
                grid[r][c] = 1
            else:
                grid[r][c] = grid[r-1][c] + grid[r][c-1]
    return grid

def find_last(grid):
    return grid[len(grid)-1][len(grid[0]) - 1]

grid = create_grid(21, 21)
grid = calc_paths(grid)
print("paths:", find_last(grid))


