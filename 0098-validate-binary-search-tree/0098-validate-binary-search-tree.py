# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        minm = float('-inf')
        maxm = float('inf')
        def isValid(root , minm , maxm):
            if not root:
                return True
            if  not minm < root.val < maxm:
                return False
            return isValid(root.left , minm , root.val) and isValid(root.right , root.val , maxm)
        return isValid(root , minm , maxm)
        