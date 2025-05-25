# Last updated: 5/25/2025, 12:07:02 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == p or root == q or root is None:
            return root

        left = self.lowestCommonAncestor(root.left, p , q)
        right = self.lowestCommonAncestor(root.right, p , q)

        if left is not None and right is not None:
            return root
        if left is not None and right is None:
            return left
        elif left is None and right is not None:
            return right
        else:
            return None
        