"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        visited = {
            p : True
        }
        if not p.parent:
            return p
        while p.parent:
            visited[p.parent] = True
            p = p.parent
        if not q.parent:
            return q
        if q in visited:
            return q
        while q and q.parent:
            if q.parent in visited:
                return q.parent
            else:
                q = q.parent
        


        