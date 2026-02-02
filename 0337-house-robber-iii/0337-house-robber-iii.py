# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traversal(self, node):
        if not node:
            return (0 , 0)
        left = self.traversal(node.left)
        right = self.traversal(node.right)
        val_0 = max(left[1] , left[0]) + max(right[1] , right[0])
        val_1 = node.val + left[0] + right[0]
        return (val_0 , val_1)

    def rob(self, root: Optional[TreeNode]) -> int:
        dp = self.traversal(root)
        return max(dp)