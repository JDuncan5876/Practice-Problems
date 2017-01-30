# Construct a binary tree from the preorder and inorder traversals of said tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        self.i = 0
        self.preorder = preorder
        self.inorder = inorder
        self.indexTable = {value:index for index, value in enumerate(inorder)}
        return self.buildTreeHelper(0, len(inorder))

    def buildTreeHelper(self, start, end):
        if start >= end:
            return None
        node = TreeNode(self.preorder[self.i])
        index = self.indexTable[self.preorder[self.i]]
        self.i += 1
        node.left = self.buildTreeHelper(start, index)
        node.right = self.buildTreeHelper(index + 1, end)
        return node