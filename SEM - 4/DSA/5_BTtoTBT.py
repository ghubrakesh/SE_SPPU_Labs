class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.is_threaded = False


def convert_to_threaded_binary_tree(root):
    if root is None:
        return None

    # Find the predecessor of each node
    predecessor = None
    def find_predecessor(node):
        nonlocal predecessor
        if node is None:
            return

        find_predecessor(node.left)

        if node.left is None:
            node.left = predecessor
            node.is_threaded = True

        if predecessor and predecessor.right is None:
            predecessor.right = node

        predecessor = node

        find_predecessor(node.right)

    find_predecessor(root)

    return root


def inorder_traversal(root):
    if root is None:
        return []

    result = []

    # Find the leftmost node
    current = root
    while current.left:
        current = current.left

    # Perform in-order traversal using threaded pointers
    while current:
        result.append(current.data)

        if current.is_threaded:
            current = current.right
        else:
            current = current.right
            while current and not current.is_threaded:
                current = current.left

    return result


# Create a binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

# Convert binary tree to threaded binary tree
threaded_root = convert_to_threaded_binary_tree(root)

# Perform in-order traversal on threaded binary tree
inorder = inorder_traversal(threaded_root)
print("In-order Traversal:", inorder)
