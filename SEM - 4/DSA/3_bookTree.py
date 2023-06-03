class Node:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child):
        self.children.append(child)
        
# Print the nodes
def print_tree(node, level=0):
    print("  " * level + "- " + node.data)
    for child in node.children:
        print_tree(child, level + 1)

book = Node("DSA")
chapter1 = Node("Hashing")
chapter2 = Node("Trees")
section1_1 = Node("Hash Table")
section1_2 = Node("Skip List")
section2_1 = Node("Binary Tree")
section2_2 = Node("AVL Tree")
subsection1_2_1 = Node("algo for skip list")
subsection2_1_1 = Node("Binary Search Tree")

book.add_child(chapter1)
book.add_child(chapter2)
chapter1.add_child(section1_1)
chapter1.add_child(section1_2)
chapter2.add_child(section2_1)
chapter2.add_child(section2_2)
section1_2.add_child(subsection1_2_1)
section2_1.add_child(subsection2_1_1)

print_tree(book)
