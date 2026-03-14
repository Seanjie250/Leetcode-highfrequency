class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        path = []
        rst = []
        open_c , close_c = n , n
        def backtracking(open_c , close_c , path):
            if close_c < 0 or open_c < 0:
                return
            if close_c < open_c:
                return
            if close_c == 0 and open_c == 0:
                rst.append(''.join(path))
            path.append('(')
            backtracking(open_c - 1 , close_c  , path)
            path.pop()
            path.append(')')
            backtracking(open_c , close_c -1 , path)
            path.pop()
            return rst
        rst = backtracking(n , n , [])
        return rst

                         