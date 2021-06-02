from Node import Node
from BinarySearchTree import BinarySearchTree


def findKthMax(root, k):
    tree = []
    inOrderTraverse(root, tree)  # Get sorted tree list
    if ((len(tree)-k) >= 0) and (k > 0):  # check if k is valid
        return tree[-k]  # return the kth max value
    return None  # return none if no value found


def inOrderTraverse(node, tree):
    # Helper recursive function to traverse the tree inorder
    if node is not None:  # check if node exists
        inOrderTraverse(node.leftChild, tree)  # traverse left sub-tree
        if len(tree) == 0:
            # Append if empty tree
            tree.append(node.val)
        elif tree[-1] is not node.val:
            # Ensure not a duplicate
            tree.append(node.val)  # add current node value
        inOrderTraverse(node.rightChild, tree)  # traverse right sub-tree


BST = BinarySearchTree(6)
BST.insert(4)
BST.insert(9)
BST.insert(5)
BST.insert(2)
BST.insert(8)
BST.insert(12)

print(findKthMax(BST.root, 3))
