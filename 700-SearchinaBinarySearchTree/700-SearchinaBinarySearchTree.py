# Last updated: 5/24/2025, 10:56:05 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def pre_order(Node,val):
            if not Node or Node.val == val:
                return Node    
            elif Node.val > val:
                return pre_order(Node.left ,val)
            elif Node.val < val:
                return pre_order(Node.right ,val)
        return pre_order(root,val)

        