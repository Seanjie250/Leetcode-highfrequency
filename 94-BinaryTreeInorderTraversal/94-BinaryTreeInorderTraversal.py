# Last updated: 5/21/2025, 1:42:15 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        levels = []

        def traverse(node,level):
            if not node:
                return 
            if len(levels) == level:
                levels.append([])
            
            levels[level].append(node.val)
            traverse(node.left,level + 1)
            traverse(node.right,level + 1)
        traverse(root,0)

        return levels
            
        