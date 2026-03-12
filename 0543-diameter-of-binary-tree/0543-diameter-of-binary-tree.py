# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = -1
        def helper(node):
            if not node:
                return -1
            if node.left:
                left = helper(node.left)
            else:
                left = 0
            if node.right:
                right = helper(node.right)
            else:
                right = 0
            maxm = max(left , right) + 1
            self.ans = max(self.ans , right + left)
            return maxm
        maxm = helper(root)
        return self.ans