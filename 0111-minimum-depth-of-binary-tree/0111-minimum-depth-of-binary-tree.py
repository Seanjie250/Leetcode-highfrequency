# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque()
        q.append(root)
        depth = 0
        while q:
            for i in range(len(q)):
                cur = q.popleft()
                if not cur.left and not cur.right:
                    return depth + 1
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            depth += 1
    


        