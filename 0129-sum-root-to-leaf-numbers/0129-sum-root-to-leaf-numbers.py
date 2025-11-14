# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traversal(self,root,path,rst):
        if not root:
            return
        path.append(root.val)

        if not root.left and  not root.right:
            rst.append(path.copy())

        self.traversal(root.left,path,rst)
        self.traversal(root.right,path,rst)

        path.pop()

        return rst
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        path = []
        rst = [] 
        self.traversal(root,path,rst)
        amount = 0
        for arr in rst:
            number = int("".join(str(x) for x in arr))
            amount += number
        return amount


