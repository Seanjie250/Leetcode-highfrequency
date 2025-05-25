# Last updated: 5/25/2025, 10:39:08 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        rst = defaultdict(int)
        def mode(Node):
            if not Node:
                return
            mode(Node.left)
            rst[Node.val] += 1
            mode(Node.right)
        mode(root)
        if not rst:
            return []
        max_freq = max(rst.values())
        return [key for key,frq in rst.items() if frq == max_freq]
            
        
        
        