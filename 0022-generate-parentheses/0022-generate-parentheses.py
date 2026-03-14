class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        path = []
        rst = []
        open_c , close_c = 0 , 0
        def backtracking(open_c , close_c , path):
            if close_c > n or open_c > n:
                return
            if close_c > open_c:
                return
            if close_c == n and open_c == n:
                rst.append(''.join(path))
            path.append('(')
            backtracking(open_c + 1 , close_c  , path)
            path.pop()
            path.append(')')
            backtracking(open_c , close_c + 1, path)
            path.pop()
            return rst
        rst = backtracking(0 , 0 , [])
        return rst

                         