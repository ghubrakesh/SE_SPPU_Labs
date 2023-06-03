class Node:
    def __init__(self, data):
        self.left = None
        self.right = None 
        self.data = data

def build_tree(prefix): 
    stack = []
    for char in reversed(prefix): 
        if char.isalpha():
            node = Node(char)
            stack.append(node) 
        else: 
            node = Node(char)
            node.left = stack.pop()
            node.right = stack.pop() 
            stack.append(node)
    return stack.pop()

def postorder(root):
    if root is None:
        return []
    stack1 = [root]
    stack2 = []

    while stack1:
        node = stack1.pop()
        stack2.append(node.data)
        if node.right:
            stack1.append(node.right)
        if node.left:
            stack1.append(node.left)

    return stack2[::-1]


prefix="--abc/def" 
root = build_tree(prefix)

#rec_postorder (root) 
print(postorder(root))