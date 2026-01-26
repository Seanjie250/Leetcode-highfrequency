class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        left = 0 
        right = m * n - 1
        
        while left <= right:
            middle = (left + right) // 2
            r , c = divmod(middle , n)
            val = matrix[r][c]
            if val == target:
                return True
            elif val > target:
                right = middle - 1
            elif val < target:
                left = middle + 1
        return False
        