def read_file():
    level = []
    tree = []

    with open("./in", "r") as f:
        for line in f:
            tree = tree + [int(x) for x in line.split(" ")]
            level = level + [[int(x) for x in  line.split(" ")]]
    return (level, tree)

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None 
        self.right = None
        self.is_leaf = False

class Path:
    def __init__(self, tree, level):
        self.tree = tree
        self.level = level
        self.root = None

    def set_root(self, root):
        self.root = root

    def build_tree(self):
        level = self.level
        tree = self.tree
        acc_idx = 0
        for r in range(1, len(level) + 1):
            for c in range(0, len(level[r - 1])):
                if isinstance(tree[acc_idx], Node) == False:
                   tree[acc_idx] = Node(tree[acc_idx])
                if acc_idx == 0:
                    self.set_root(tree[acc_idx])
                if acc_idx + r >= len(tree):
                    tree[acc_idx].is_leaf = True
                    tree[acc_idx].is_leaf = True
                else:
                    if isinstance(tree[acc_idx + r], Node) == False and tree[acc_idx + r] >= 0:
                        tree[acc_idx+r] = Node(tree[acc_idx+r])
                    if isinstance(tree[acc_idx + r + 1], Node) == False and tree[acc_idx + r + 1] >= 0:
                        tree[acc_idx+r+1] = Node(tree[acc_idx+r+1])
                    tree[acc_idx].left = tree[acc_idx+r]
                    tree[acc_idx].right = tree[acc_idx+r+1]
                acc_idx = acc_idx + 1

    def max_path_sum(self, node):
        if node == None:
            return 0
        if node.is_leaf == True:
            return node.val
        left_sum = self.max_path_sum(node.left)
        right_sum = self.max_path_sum(node.right)
        return max(left_sum, right_sum) + node.val

    def calc_max(self):
        self.build_tree()
        return self.max_path_sum(self.root)
    

level, tree = read_file()
path = Path(tree, level)
print(path.calc_max())
            
