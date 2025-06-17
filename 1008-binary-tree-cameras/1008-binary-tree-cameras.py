# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traversal(self,node,rst):
        if not node:
            return 2
        left = self.traversal(node.left,rst)
        right = self.traversal(node.right,rst)

        if left == 2 and right == 2:
            return 0
        
        if left == 0 or right == 0:
            rst[0] += 1
            return 1

        if left == 1 or right ==1:
            return 2
        

    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        rst = [0]
        if self.traversal(root,rst) == 0:
            rst[0] += 1
        return rst[0]

        
        