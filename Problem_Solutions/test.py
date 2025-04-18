"""
Problem 1: Monstera Madness
Given the root of a binary tree where each node represents the number of splits in a leaf of a Monstera plant, 
return the number of Monstera leaves that have an odd number of splits.

Evaluate the time complexity of your function. 
Define your variables and provide a rationale for why you believe your solution has the stated time complexity.
"""
from collections import deque

class TreeNode():
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def print_tree(root):
    if not root:
        return "Empty"
    
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    print(result)


def build_tree(values):
    if not values:
        return None

    def get_key_value(item):
        if isinstance(item, tuple):
            return item[0], item[1]
        else:
            return None, item

    key, value = get_key_value(values[0])
    root = TreeNode(value, key)
    queue = deque([root])
    index = 1

    while queue:
        node = queue.popleft()
        if index < len(values) and values[index] is not None:
            left_key, left_value = get_key_value(values[index])
            node.left = TreeNode(left_value, left_key)
            queue.append(node.left)
        index += 1
        if index < len(values) and values[index] is not None:
            right_key, right_value = get_key_value(values[index])
            node.right = TreeNode(right_value, right_key)
            queue.append(node.right)
        index += 1

    return root

'''         
def preorder_traversal(node):
    if node is None:
        return 0
    
    # Process current node
    if node.val % 2 == 1:
        ...
    
    # Recursively traverse left subtree
    preorder_traversal(node.left)
    
    # Recursively traverse right subtree
    preorder_traversal(node.right)
'''


def count_odd_splits(root):
    if not root:
        return 0

    left, right = count_odd_splits(root.left), count_odd_splits(root.right)

    if root.val % 2 != 0:
        return 1 + left + right

    else:
        return left + right
    # if there is no root, return none


# Using build_tree() function included at top of page
values = [2, 3, 5, 6, 7, None, 12]
monstera = build_tree(values)

print(count_odd_splits(monstera))
print(count_odd_splits(None))

"""
# results
3
0
"""