class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m , n = len(matrix) , len(matrix[0])
        up_bound , bottom_bound = 0 , m - 1
        left_bound  , right_bound = 0 , n - 1
        rst = []
        while len(rst) < m * n:
            if up_bound <= bottom_bound:
                for i in range(left_bound , right_bound + 1):
                    rst.append(matrix[up_bound][i])
                up_bound += 1
            if right_bound >= left_bound:
                for i in range(up_bound , bottom_bound + 1):
                    rst.append(matrix[i][right_bound])
                right_bound -= 1
            if up_bound <= bottom_bound:
                for i in range(right_bound , left_bound - 1, -1):
                    rst.append(matrix[bottom_bound][i])
                bottom_bound -= 1
            if right_bound >= left_bound:
                for i in range(bottom_bound , up_bound - 1 ,  -1):
                    rst.append(matrix[i][left_bound])
                left_bound += 1
        
        return rst
                 
                 