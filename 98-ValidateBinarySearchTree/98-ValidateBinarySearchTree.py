# Last updated: 5/24/2025, 11:34:07 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validrange(Node,maxm,minm):
            if not Node:
                return True
            if not minm < Node.val < maxm:
                return False
            return validrange(Node.left,Node.val,minm) and validrange(Node.right,maxm,Node.val)
 
        maxm = float('inf')
        minm = float('-inf')
        return validrange(root,maxm,minm)
                

        