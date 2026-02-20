# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(root , maxm , minm):
            if not root:
                return True
            if not root.val < maxm or not root.val > minm:
                return False
            return isValid(root.left , root.val , minm) and isValid(root.right , maxm , root.val)
        
        return isValid(root , float('inf') ,  float('-inf') )
        
