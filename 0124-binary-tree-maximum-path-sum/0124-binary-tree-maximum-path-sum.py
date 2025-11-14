# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxval = [float('-inf')]

        def dfs(node):
            if not node:
                return 0

            # compute downward max from left and right
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)

            # update global
            maxval[0] = max(maxval[0], node.val + left + right)

            # return single-branch path
            return node.val + max(left, right)

        dfs(root)
        return maxval[0]



        