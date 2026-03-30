class TreeNode:
    def __init__(self , left , right , val):
        self.left = None
        self.right = None
        self.val = val
class Solution:
    def diameterOfBinaryTree(self , root):
        self.maxm = float('-inf')
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            self.maxm = max(self.maxm , left + right)
            return 1 + max(left , right)
        dfs(root)
        return self.maxm
        