# Last updated: 5/22/2025, 9:25:24 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def getHeightmin(Node):
            Height = 1
            if not Node:
                return Height
            elif Node.right and Node.left:
                Height = min(getHeightmin(Node.right) , getHeightmin(Node.left)) + 1
            elif Node.right and not Node.left:
                Height = getHeightmin(Node.right) + 1
            elif  not Node.right and  Node.left:
                Height = getHeightmin(Node.left) + 1
            return Height
        return getHeightmin(root)


        