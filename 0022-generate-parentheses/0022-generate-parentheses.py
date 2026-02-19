class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        path = []
        rst = []
        def backtracking(open_use , close_use , n,path):
            if open_use == n and close_use == n:
                rst.append(''.join(path))
            if open_use < close_use:
                return 
            if open_use < n:
                path.append('(')
                backtracking(open_use + 1, close_use , n , path)
                path.pop()
            if close_use < n:
                path.append(')')
                backtracking(open_use, close_use + 1 , n , path)
                path.pop()
        backtracking(0 , 0 , n , path)
        return rst
        