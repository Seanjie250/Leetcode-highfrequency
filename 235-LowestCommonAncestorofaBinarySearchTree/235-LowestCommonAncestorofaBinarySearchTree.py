# Last updated: 5/26/2025, 10:45:40 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            Node = TreeNode(val)
            return Node

        if val > root.val:
            root.right = self.insertIntoBST(root.right,val)
        if val < root.val:
            root.left = self.insertIntoBST(root.left,val)
        return root


        