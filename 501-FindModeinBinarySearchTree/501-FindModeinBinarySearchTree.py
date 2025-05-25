# Last updated: 5/25/2025, 11:36:46 AM
class TreeNode:
    def __int__(self,x):
        self.val = x
        self.right = None
        self.left = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == q or root == p or root is None:
            return root
        
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)

        if left is not None and right is not None:
            return root
        if left is not None and right is None:
            return left
        elif right is not None and left is None:
            return right
        else:
            return None
        
        

        
        