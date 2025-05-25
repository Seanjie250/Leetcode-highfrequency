# Last updated: 5/25/2025, 10:20:03 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.prev = None
        self.min_dif = float('inf')
        def inorder(Node):
            if not Node:
                return
            inorder(Node.left)
            if self.prev is not None:
                self.min_dif = min(abs(Node.val - self.prev),self.min_dif)
            self.prev = Node.val
            inorder(Node.right)
        inorder(root)
        return self.min_dif


        


        
        
        