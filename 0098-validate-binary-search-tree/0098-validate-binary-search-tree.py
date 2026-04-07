# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        maxm = float('inf')
        minm = float('-inf')
        def isvalid(node , maxm , minm):
            if not node:
                return True
            if not minm < node.val < maxm:
                return False
            return isvalid(node.left , node.val , minm) and isvalid(node.right , maxm , node.val)
        return isvalid(root , maxm , minm)
        