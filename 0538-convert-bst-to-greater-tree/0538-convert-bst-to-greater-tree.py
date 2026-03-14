# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        ans = 0
        def postorder(root):
            nonlocal ans
            if not root:
                return
            postorder(postorder(root.right))
            ans += root.val
            root.val = ans
            postorder(postorder(root.left))
        postorder(root)
        return root