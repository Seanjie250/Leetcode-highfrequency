from  bisect  import bisect_left
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m , n = len(matrix) , len(matrix[0])
        for i in range(m):
            if matrix[i][0] <= target and matrix[i][-1] >= target:
                index = bisect_left(matrix[i] , target)
                if matrix[i][index] == target:
                    return True 
        return False
                

        