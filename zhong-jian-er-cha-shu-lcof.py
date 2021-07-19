# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        if len(preorder) == 0:
            return None
        root = TreeNode(preorder[0])
        pos = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:pos+1], inorder[:pos])
        root.right = self.buildTree(preorder[pos+1:], inorder[pos+1:])
        return root
