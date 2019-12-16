# https://www.testdome.com/questions/python/binary-search-tree/14288?questionIds=17253,14288,14246,14245&generatorId=93&type=fromtest&testDifficulty=Easy

# Binary search tree (BST) is a binary tree where the value of each node is larger or equal to the values in
# all the nodes in a that node's left subtree and is smaller than the values in all the nodes in that node's
# right subtree
# Write a function that checks if a given binary search tree contains a given value
# For example, for the following tree
# - n1 (Value:1, Left:null, Right:null)
# - n2 (Value:2, Left:n1, Right:n3)
# - n3 (Value:3, Left:null, Right:null)
# Call to contains(n2,3) should return True since a tree with root at n2 contains number 3

import collections

class BinarySearchTree:
    Node = collections.namedtuple('Node', ['left', 'right', 'value'])

    @staticmethod
    def contains(root, value):
        if root.value == value:return True
        if root.left:
            if root.left.value == value:return True
        if root.right:
            if root.right.value == value:return True

        return False

n1 = BinarySearchTree.Node(value=1, left=None, right=None)
n3 = BinarySearchTree.Node(value=3, left=None, right=None)
n2 = BinarySearchTree.Node(value=2, left=n1, right=n3)

print(BinarySearchTree.contains(n2, 3))
