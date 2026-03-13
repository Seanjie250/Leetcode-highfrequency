# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        rst = [root.val]
        def is_leaf(node):
            return not node.left and not node.right
        node = root.left
        while node:
            if not node:
                return
            if not is_leaf(node):
                rst.append(node.val)
            if node.left:
                node = node.left
            else:
                node = node.right
        def dfs(node):
            if not node:
                return 
            if is_leaf(node):
                rst.append(node.val)
                return
            dfs(node.left)
            dfs(node.right)

        dfs(root.left)
        dfs(root.right)
        stack = []
        node = root.right
        while node:
            if not is_leaf(node):
                stack.append(node.val)
            if node.right:
                node = node.right
            else:
                node = node.left
        return rst + stack[::-1]

                