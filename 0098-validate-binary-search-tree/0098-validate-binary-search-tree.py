# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        maxm , minm = float('inf') , float('-inf')
        def isValid(node , maxm , minm):
            if not node:
                return True
            if not minm < node.val < maxm:
                return False
            return isValid(node.left , node.val , minm) and isValid(node.right , maxm , node.val)
        return isValid(root , maxm , minm )

        