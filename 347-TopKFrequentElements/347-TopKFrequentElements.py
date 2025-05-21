# Last updated: 5/21/2025, 9:26:13 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def DFS(Node):
            if Node is None:
                return []
            
            result.append(Node.val)
            DFS(Node.left)
            DFS(Node.right)
        DFS(root)
        return result
            
        
        