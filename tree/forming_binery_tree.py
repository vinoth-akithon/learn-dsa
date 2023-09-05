class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def create_binary_tree(input_str):
    values = input_str.split()
    if not values:
        return None

    root = TreeNode(int(values[0]))
    queue = [root]
    i = 1

    while i < len(values):
        parent = queue.pop(0)

        left_val = values[i]
        i += 1
        if left_val != 'N':
            parent.left = TreeNode(int(left_val))
            queue.append(parent.left)

        if i < len(values):
            right_val = values[i]
            i += 1
            if right_val != 'N':
                parent.right = TreeNode(int(right_val))
                queue.append(parent.right)

    return root

# Example usage:
input_str = "4 5 2 N N 3 1 6 7"
root = create_binary_tree(input_str)