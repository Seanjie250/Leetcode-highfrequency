# Last updated: 5/22/2025, 10:19:12 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def getheight(Node) -> int:
            if not Node:
                return 0
            if (left_height := getheight(Node.left)) == -1:
                return -1
            if (right_height := getheight(Node.right)) == -1:
                return -1
            if abs(left_height - right_height) > 1:
                return -1
            else:
                return 1 + max(left_height,right_height)

        return True if getheight(root) != -1 else False
            
