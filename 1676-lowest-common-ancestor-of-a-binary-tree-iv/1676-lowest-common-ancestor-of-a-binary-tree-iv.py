# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findcommonancestor(self , node , p , q):
        if not node:
            return 
        if node == q or node == p:
            return node
        left = self.findcommonancestor(node.left , p , q)
        right =self.findcommonancestor(node.right , p , q)
        if left and right:
            return node
        elif not left:
            return right
        elif not right:
            return left
        
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        if len(nodes) == 1:
            return nodes[0]
        que = deque(node for node in nodes)
        while len(que) >= 2:
            p = que.popleft()
            q = que.popleft()
            que.append(self.findcommonancestor(root , p , q))
        return que.popleft()


            

        