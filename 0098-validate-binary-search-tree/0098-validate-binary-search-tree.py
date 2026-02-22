# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        maxm , minm = float('inf') , float('-inf')
        def is_ok(root , maxm , minm):
            if not root:
                return True
            if root.val >= maxm or root.val <= minm:
                return False
            
            return is_ok(root.left , root.val , minm) and is_ok(root.right , maxm , root.val)
        
        return is_ok(root , maxm , minm)
        