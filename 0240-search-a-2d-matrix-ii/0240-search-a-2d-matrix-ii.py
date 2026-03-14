class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = []
        for i in range(len(matrix)):
            if matrix[i][0] <= target <= matrix[i][-1]:
                l.append(i)
        if l == []:
            return False
        for row in l:
            left , right = 0 , len(matrix[0]) - 1
            while left <= right:
                mid = (left + right) // 2
                if matrix[row][mid] == target:
                    return True
                elif matrix[row][mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
        return False

        