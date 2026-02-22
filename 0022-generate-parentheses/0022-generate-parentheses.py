class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        left_left, right_left = n , n
        path = []
        rst = []
        def backtracking(path ,rst, left , right):
            if left == 0 and right == 0:
                rst.append(''.join(path))
            if left > right:
                return 
            if left > 0 :
                path.append('(')
                backtracking(path , rst , left - 1, right)
                path.pop()
            if right > 0:
                path.append(')')
                backtracking(path , rst , left, right - 1)
                path.pop()
            
        backtracking(path ,rst , left_left , right_left)
        return rst


        