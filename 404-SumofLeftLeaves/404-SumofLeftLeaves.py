# Last updated: 5/22/2025, 1:20:13 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def sumofleft(Node) -> int:
            val = 0
            if not Node:
                return 0
            if Node.left:
                tmp = Node.left
                if not tmp.left and not tmp.right:
                    val += tmp.val 
                else:
                    val += sumofleft(Node.left)
            if Node.right:
                val += sumofleft(Node.right)
            return val

        return sumofleft(root)
            

        