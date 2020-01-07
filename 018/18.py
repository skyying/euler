

    
def read_file():
    level = []
    tree = []

    with open("./in", "r") as f:
        for line in f:
            tree = tree + [int(x) for x in line.split(" ")]
            level = level + [[int(x) for x in  line.split(" ")]]
    return (level, tree)
            




def max_path_sum():
    level, tree = read_file()
    print(level)
    print(tree)
    acc_idx = 0
    for r in range(1, len(level) + 1):
        for c in range(0, len(level[r - 1])):
            node = (tree[acc_idx], tree[acc_idx+r], tree[acc_idx+r+1])
            acc_idx = acc_idx + 1
            
            
max_path_sum()
