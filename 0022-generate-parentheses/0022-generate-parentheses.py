class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        path = []
        open_left , close_left = n , n
        rst = []
        def backtracking(open_left , close_left , path):
            if len(path) == n * 2:
                rst.append(''.join(path))
                return
            if open_left > 0:
                path.append('(')
                backtracking(open_left - 1 , close_left , path)
                path.pop()
            if close_left > 0 and open_left < close_left:
                path.append(')')
                backtracking(open_left , close_left  - 1, path)
                path.pop()
            return rst
        rst = backtracking(open_left , close_left , path)
        return rst
