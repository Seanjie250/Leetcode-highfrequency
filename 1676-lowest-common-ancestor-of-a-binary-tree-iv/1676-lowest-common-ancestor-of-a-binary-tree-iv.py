# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:        
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        seen = set(nodes)
        if not root or root in seen:
            return root
        
        leftlca = self.lowestCommonAncestor(root.left , nodes)
        rightlca = self.lowestCommonAncestor(root.right , nodes)

        if leftlca and rightlca:
            return root
        elif not leftlca:
            return rightlca
        elif not rightlca:
            return leftlca


            

        