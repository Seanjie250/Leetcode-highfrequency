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
       
        def getNode(root):
            total = 1
            if not root:
                return 0
            elif root.left or root.right:
                total = getNode(root.left) + getNode(root.right) + 1
            return total
        num = getNode(root)
        return num