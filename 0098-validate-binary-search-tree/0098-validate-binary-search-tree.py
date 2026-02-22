# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        maxm  , minm = float('inf') , float('-inf')
        def checkifvalid(node , maxm , minm):
            if not node:
                return True
            if node.val >=  maxm or node.val <= minm:
                return False
            return checkifvalid(node.left , node.val , minm) and checkifvalid(node.right , maxm , node.val)

        return checkifvalid(root ,maxm , minm)

        