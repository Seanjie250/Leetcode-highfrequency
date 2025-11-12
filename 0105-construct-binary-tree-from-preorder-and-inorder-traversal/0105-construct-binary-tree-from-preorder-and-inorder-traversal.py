# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        root_val = preorder[0]
        root = TreeNode(val = root_val)

        index = inorder.index(root_val)

        leftinorder = inorder[:index]
        rightinorder = inorder[index + 1 :]

        leftpreorder = preorder[1:len(leftinorder) + 1]
        rightpreorder = preorder[len(leftinorder) + 1:]

        root.left = self.buildTree(leftpreorder , leftinorder)
        root.right = self.buildTree(rightpreorder , rightinorder)

        return root


        