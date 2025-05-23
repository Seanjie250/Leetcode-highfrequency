# Last updated: 5/23/2025, 9:34:00 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not postorder:
            return None
        root_val = postorder[-1]
        root = TreeNode(root_val)
        seperate = inorder.index(root_val)

        leftinorder = inorder[:seperate]
        rightinorder = inorder[seperate + 1:]

        postorder.pop()

        leftpostorder = postorder[:len(leftinorder)]  
        rightpostorder = postorder[len(leftinorder):]    

        root.left = self.buildTree(leftinorder,leftpostorder)
        root.right = self.buildTree(rightinorder,rightpostorder)
        
        return root
        