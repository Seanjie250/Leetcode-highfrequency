# Last updated: 5/22/2025, 9:47:58 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def getNode(Node):
            Total = 1
            if not Node:
                return 0
            elif Node.left or Node.right:
                Total = getNode(Node.left) + getNode(Node.right) + 1
            return Total
        return getNode(root)
        



            


        