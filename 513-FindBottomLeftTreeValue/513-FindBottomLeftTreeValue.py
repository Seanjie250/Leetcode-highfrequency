# Last updated: 5/22/2025, 2:26:21 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        self.result = 0
        self.max_depth = float('-inf')
        self.traversal(root,0)
        return self.result

    def traversal(self,Node,depth):
        if not Node.left and not Node.right:
            if depth > self.max_depth:
                self.max_depth = depth
                self.result = Node.val
            return 
        if Node.left:
            self.traversal(Node.left,depth + 1)
        if Node.right:
            self.traversal(Node.right,depth + 1)



        