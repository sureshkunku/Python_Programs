class TreeNode:
    def __init__(self,  value):
        self.value = value
        self.left = None
        self.right = None

def Tree_search(root, target):

    if root is None:
        return  -1

    if root.value == target:
        return target

    left = Tree_search(root.left, target)
    right = Tree_search(root.right, target)

    return left or right



# Example usage
# Create a binary tree
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(8)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

# Search for a target value using DFS
target = 4
found = Tree_search(root, target)

if found:
    print(f"Target value {target} found in the tree.")
else:
    print(f"Target value {target} not found in the tree.")