"""
Python iterative solution to delete the node of a binary search tree
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        node = root
        parent = None
        while (node and node.val != key):
            parent = node
            if key < node.val:
                node = node.left
            elif key > node.val:
                node = node.right
        if not node:
            return root
        if not node.left and not node.right:
            newChild = None
        elif node.left and not node.right:
            newChild = node.left
        elif not node.left and node.right:
            newChild = node.right
        else:
            newChild = node.left
            oldParent = node
            while newChild.right:
                oldParent = newChild
                newChild = newChild.right
            if oldParent != node:
                oldParent.right = newChild.left
                newChild.left = node.left
            newChild.right = node.right
        if not parent:
            root = newChild
        elif parent.left == node:
            parent.left = newChild
        else:
            parent.right = newChild
        return root