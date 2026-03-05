class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        open_c , close_c = 0 , 0
        path = []
        rst = []
        def backtracking(open_c , close_c , path , rst):
            
            if open_c < 0 or close_c < 0:
                return 
            if close_c < open_c:
                return 
            if close_c == 0 and open_c == 0:
                rst.append(''.join(path))

            
            path.append('(')
            backtracking(open_c - 1 , close_c , path,rst)
            path.pop()

            path.append(')')
            backtracking(open_c , close_c - 1 , path,rst)
            path.pop()
            return rst

        backtracking(n , n ,path,rst)
        return rst
        
        
        