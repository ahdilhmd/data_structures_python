class Node:
    def __init__(self, value):
        self.value = value
        self.left = None 
        self.right = None
    
class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def preorder_traversal(self, root, traversal):
        if root:
            traversal.append(root.value)
            self.preorder_traversal(root.left, traversal)
            self.preorder_traversal(root.right, traversal)
        return traversal


    def inorder_traversal(self, root, traversal):
        if root:
            self.inorder_traversal(root.left, traversal)
            traversal.append(root)
            self.inorder_traversal(root.left, traversal)

# Structure of the Binary Tree
#         1
#       /  \
#      2    3 
#     / \  / \
#    4  5 6  7
#
#

## Constructing the Binary Tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)



preorder_traversal = tree.preorder_traversal(tree.root, [])
print(preorder_traversal)

inorder_traversal = tree.inorder_traversal(tree.root, [])
print(inorder_traversal)