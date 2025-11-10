class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def getHeight(node):
            if not node:
                return 0
            return max(getHeight(node.left), getHeight(node.right)) + 1
        return getHeight(root)
