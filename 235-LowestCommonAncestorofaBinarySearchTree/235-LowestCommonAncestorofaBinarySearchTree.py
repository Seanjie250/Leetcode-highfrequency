# Last updated: 5/25/2025, 12:17:42 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def traversal(Node,p,q):
            if not Node:
                return None
            if Node.val > p.val and Node.val > q.val:
                left = traversal(Node.left,p,q)
                if left is not None:
                    return left
            if Node.val < p.val and Node.val < q.val:
                right = traversal(Node.right,p,q)
                if right is not None:
                    return right
            else:
                return Node
        return traversal(root,p,q)
                
            
        