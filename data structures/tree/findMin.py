from Node import Node
from BinarySearchTree import BinarySearchTree


def findMin(root):

    if root.leftChild is None:
        return root.val
    if root.leftChild is not None:
        result = findMin(root.leftChild)
        return result


BST = BinarySearchTree(6)
BST.insert(20)
BST.insert(-1)

print(findMin(BST.root))
