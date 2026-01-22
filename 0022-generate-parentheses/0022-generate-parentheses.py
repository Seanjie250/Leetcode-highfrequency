class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        rst = []
        path = []

        def dfs(open_int , close_int):
            if len(path) == 2 * n:
                rst.append(''.join(path))
                return
            if open_int < n:
                path.append('(')
                dfs(open_int + 1 , close_int)
                path.pop()
            if close_int < open_int:
                path.append(')')
                dfs(open_int , close_int + 1)
                path.pop()
        dfs(0,0)
        return rst
        