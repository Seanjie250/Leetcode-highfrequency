# Last updated: 5/23/2025, 4:35:39 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def merge(Node1,Node2):

            if Node1 and Node2:
                new_node = TreeNode()
                new_node.val = Node1.val + Node2.val
            elif Node1 and not Node2:
                new_node = TreeNode()
                new_node.val = Node1.val
            elif not Node1 and  Node2:
                new_node = TreeNode()
                new_node.val = Node2.val
            elif not Node1 and not Node2:
                return None
            new_node.left = merge(Node1.left if Node1 else None,Node2.left if Node2 else None)
            new_node.right = merge(Node1.right if Node1 else None,Node2.right if Node2 else None)
            return new_node

        return merge(root1,root2)
        
        
        