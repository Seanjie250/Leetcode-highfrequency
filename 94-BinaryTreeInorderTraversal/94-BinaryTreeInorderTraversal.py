# Last updated: 5/21/2025, 1:21:36 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        rst = []
        stack = []
        if not root:
            return []
        stack.append(root)
        while stack:
            node = stack.pop()
            rst.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        rst.reverse()
        return rst

        