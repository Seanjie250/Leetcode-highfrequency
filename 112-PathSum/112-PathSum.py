# Last updated: 5/22/2025, 4:03:03 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traversal(self,Node,path,rst) -> List[int]:
        path.append(Node.val)
        if not Node.left and not Node.right:
            rst.append(sum(path))
            return
        if Node.left:
            self.traversal(Node.left,path,rst)
            path.pop()
        if Node.right:
            self.traversal(Node.right,path,rst)
            path.pop()
        return rst
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if root and not root.left and not root.right and root.val == targetSum:
            return True
        elif root and not root.left and not root.right and root.val != targetSum:
            return False
        path = []
        rst = []
        return True if targetSum in self.traversal(root,path,rst) else False

        

        