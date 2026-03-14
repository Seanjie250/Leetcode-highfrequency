class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        target_row = -1
        for i in range(len(matrix)):
            if matrix[i][0] <= target <= matrix[i][-1]:
                target_row = i
                break
        if target_row == -1:
            return False
        left , right = 0 , len(matrix[0]) - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[target_row][mid] == target:
                return True
            elif matrix[target_row][mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False