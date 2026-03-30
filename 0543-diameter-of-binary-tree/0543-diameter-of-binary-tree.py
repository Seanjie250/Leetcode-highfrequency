class TreeNode:
    def __init__(self , val):
        self.left = None
        self.right = None
        self.val = val
def tree_build(arr):
    if not arr or arr[0] == - 1:
        return None
    root = TreeNode(arr[0])
    queue = [root]
    i = 1
    while queue and i < len(arr):
        node = queue.pop(0)
        if queue and arr[i] != -1:
            node.left = TreeNode(arr[i])
            queue.append(node.left)
        i += 1
        if queue and arr[i] != -1:
            node.right = TreeNode(arr[i])
            queue.append(node.right)
        i += 1
    return root
class Solution:
    def diameterOfBinaryTree(self , root):
        self.maxm = float('-inf')
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            self.maxm = max(self.maxm , left + right)
            return 1 + max(left , right)
        dfs(root)
        return self.maxm
    
arr = [1, 2, 3, 4, 5]
root = tree_build(arr)
ans = Solution().diameterOfBinaryTree(root)
print(ans)