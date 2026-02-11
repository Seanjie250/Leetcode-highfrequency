# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:    
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        levels = []
        def traversal(node,level):
            if not node:
                return 
            if len(levels) == level:
                levels.append([])
            levels[level].append(node.val)
            traversal(node.left , level + 1)
            traversal(node.right , level + 1)
            return levels
        ans = traversal(root, 0)
        return ans
            

            



        
        
            

        
        
        
        