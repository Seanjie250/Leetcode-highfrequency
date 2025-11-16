# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p == root or q == root:
            return root
        if not root:
            return None
        left = self.lowestCommonAncestor(root.left , p, q)
        right = self.lowestCommonAncestor(root.right , p, q)

        if left and right:
            return root
        if left and not right:
            return left
        elif right and not left:
            return right
        else:
            return None
        