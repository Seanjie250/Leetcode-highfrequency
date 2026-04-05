class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        left , right = n , n
        path = []
        rst = []
        def dfs(left , right):
            if len(path) == n * 2:
                rst.append(''.join(path))
                return
            if left > 0:
                path.append('(')
                dfs(left - 1, right)
                path.pop()
            if left < right:
                path.append(')')
                dfs(left , right - 1)
                path.pop()
        dfs(left , right)
        return rst
        