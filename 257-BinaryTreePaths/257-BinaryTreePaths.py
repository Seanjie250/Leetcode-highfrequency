# Last updated: 5/22/2025, 12:37:52 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traversal(self,node,path,rst) -> List[str]:
        path.append(node.val)
        if not node.right and not node.left:
            st_path = '->'.join(map(str,path))
            rst.append(st_path)
            return
        if node.left:
            self.traversal(node.left,path,rst)
            path.pop()
        if node.right:
            self.traversal(node.right,path,rst)
            path.pop()
        return rst
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        elif not root.right and not root.left:
            rst = []
            rst.append(str(root.val))
            return rst
        rst = self.traversal(root,[],[])
        return rst



        