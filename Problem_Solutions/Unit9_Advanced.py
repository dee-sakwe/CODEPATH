from collections import deque 

# Tree Node class
class TreeNode:
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

"""
Problem 1: Croquembouche II
You are designing a delicious croquembouche (a French dessert composed of a cone-shaped tower of cream puffs 😋), for a couple's wedding. 
They want the cream puffs to have a variety of flavors. You've finished your design and want to send it to the couple for review.

Given a root of a binary tree design where each node in the tree represents a cream puff in the croquembouche, 
traverse the croquembouche in tier order (i.e., level by level, left to right).

You should return a list of lists where each inner list represents a tier 
(level) of the croquembouche and the elements of each inner list contain the flavors of each cream puff on that tier (node vals from left to right).

Note: The build_tree() and print_tree() functions both use variations of a level order traversal. 
To get the most out of this problem, we recommend that you reference these functions as little as possible while implementing your solution.

Evaluate the time and space complexity of your function. 
Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity. 
Assume the input tree is balanced when calculating time complexity.

Hint: Level order traversal, BST
"""

class Puff():
    def __init__(self, flavor, left=None, right=None):
        self.val = flavor
        self.left = left
        self.right = right

def listify_design(design):
    # Understand: perform a BFS of the tree and return the result as a list of lists containing all nodes on the same level
    # Match: BFS

    # Plan: I don't know how to do this yet, so I'll look at the functions for inspiration.

    # Implement:
    # Keep track of the level

    # level = 0

    queue = deque([design])

    # We will return this
    result = []

    while queue:
        length = len(queue)
        # store all the values in the current level
        current_level = []


        for _ in range(length):
            node = queue.popleft()

            current_level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            

        result.append(current_level)

    return result


croquembouche = Puff("Vanilla", 
                    Puff("Chocolate", Puff("Vanilla"), Puff("Matcha")), 
                    Puff("Strawberry"))

# print(listify_design(croquembouche))

"""
[['Vanilla'], ['Chocolate', 'Strawberry'], ['Vanilla', 'Matcha']]
"""

"""
Problem 2: Icing Cupcakes in Zigzag Order
You have rows of cupcakes represented as a binary tree cupcakes where each node in the tree represents a cupcake. 
To ice them efficiently, you are icing cupcakes one row (level) at a time, in zig zag order 
(i.e., from left to right, then right to left for the next row and alternate between).

Return a list of the cupcake values in the order you iced them.

Evaluate the time and space complexity of your function. 
Define your variables and provide a rationale for why you 
believe your solution has the stated time and space complexity. 
Assume the input tree is balanced when calculating time complexity.
"""

def zigzag_icing_order(cupcakes):
    if not cupcakes:
        return []
        
    # We will return this
    result = []
    
    # Initialize queue with just the root node
    queue = deque([cupcakes])
    
    # Flag to determine direction
    left_to_right = True
    
    while queue:
        level_size = len(queue)
        # Store the current level values
        current_level = []
        
        # Process all nodes at current level
        for _ in range(level_size):
            node = queue.popleft()
            
            # Add children to queue for next level
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
            # Add value to current level
            current_level.append(node.val)
        
        # Add level values to result according to direction
        if not left_to_right:
            current_level.reverse()
            
        result.extend(current_level)
        
        # Toggle direction for next level
        left_to_right = not left_to_right
    
    return result

# Using build_tree() function included at top of page
flavors = ["Chocolate", "Vanilla", "Lemon", "Strawberry", None, "Hazelnut", "Red Velvet"]
cupcakes = build_tree(flavors)

print(zigzag_icing_order(cupcakes))

"""
Output: ['Chocolate', 'Lemon', 'Vanilla', 'Strawberry', 'Hazelnut', 'Red Velvet']
"""
