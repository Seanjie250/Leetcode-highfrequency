# Last updated: 5/26/2025, 11:12:34 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val == key:
            if not root.left and not root.right:
                return None
            elif not root.left and root.right:
                return root.right
            elif not root.right and root.left:
                return root.left
            else:
                tmp = root.right
                while tmp.left:
                    tmp = tmp.left
                tmp.left = root.left
                return root.right
        if root.val > key:
            root.left = self.deleteNode(root.left,key)
        if root.val < key:
            root.right = self.deleteNode(root.right,key)
        return root
                
                



        

        