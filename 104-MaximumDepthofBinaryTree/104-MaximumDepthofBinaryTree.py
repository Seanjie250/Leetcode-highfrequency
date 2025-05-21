# Last updated: 5/21/2025, 3:05:10 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def getHeight(Node):
            Height = 1
            if not Node:
                return 0
            elif Node.left or Node.right:
                Height = max(getHeight(Node.left),getHeight(Node.right)) + 1
            return Height
        return getHeight(root)
            