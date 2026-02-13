# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bfs(self, node , target):
        if not node:
            return False
        if node == target:
            return True
        return (self.bfs(node.left , target) or self.bfs(node.right , target))

        
        
    def findcommonancestor(self ,node , p , q):
        if not node:
            return 
        if node == p or node == q:
            return node
        left = self.findcommonancestor(node.left , p , q)
        right = self.findcommonancestor(node.right , p , q)
        if left and right:
            return node
        elif not left:
            return right
        elif not right:
            return left
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not (self.bfs(root , p) and self.bfs(root , q)):
            return None
        node = self.findcommonancestor(root , p , q)
        return node
        

        