# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.sum = 0
        def traversal(Node):
            if not Node:
                return 
            traversal(Node.right)
            Node.val += self.sum
            self.sum = Node.val
            traversal(Node.left)
        traversal(root)
        return root
        
            

        