from Node import Node
from BinarySearchTree import BinarySearchTree


def inOrder(root):

    # Set current to root of binary tree
    current = root
    stack = []  # initialize stack
    done = 0
    result = []

    while True:
        # Reach the left most Node of the current Node
        if current is not None:

            # Place pointer to a tree node on the stack
            # before traversing the node's left subtree
            stack.append(current)

            current = current.leftChild

        # BackTrack from the empty subtree and visit the Node
        # at the top of the stack; however, if the stack is
        # empty you are done
        elif(stack):
            current = stack.pop()
            # Python 3 printing
            result.append(current.val)
            # We have visited the node and its left
            # subtree. Now, it's right subtree's turn
            current = current.rightChild

        else:
            return result


def findKthMax(root, k):
    result = inOrder(root)
    return result[-k]


BST = BinarySearchTree(6)
BST.insert(4)
BST.insert(9)
BST.insert(5)
BST.insert(2)
BST.insert(8)
BST.insert(12)

print(findKthMax(BST.root, 3))
