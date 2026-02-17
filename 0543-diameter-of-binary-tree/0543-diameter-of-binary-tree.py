# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans = 0

    def maxDepth(self , node):
        if not node:
            return 0
        left = self.maxDepth(node.left)
        right = self.maxDepth(node.right)

        self.ans = max(self.ans, left + right)

        return max(left , right) + 1

    def diameterOfBinaryTree(self, root):
        self.ans = 0
        self.maxDepth(root)
        return self.ans


        