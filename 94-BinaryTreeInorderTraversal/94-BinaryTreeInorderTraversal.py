# Last updated: 5/21/2025, 9:30:36 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        rst = []
        def DFS(Node):
            if Node is None:
                return 
            
            DFS(Node.left)
            rst.append(Node.val)
            DFS(Node.right)

        DFS(root)
        return rst
        