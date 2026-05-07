class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        m , n = len(matrix) , len(matrix[0])

        def count_smaller(x):
            row = m - 1
            col = 0
            count = 0
            while row >= 0 and col < n:
                if matrix[row][col] <= x:
                    count += row + 1
                    col += 1
                else:
                    row -= 1
            return count
        
        left = matrix[0][0]
        ans = - 1
        right = matrix[m - 1][n - 1]
        while left <= right:
            mid = (left + right) // 2
            if count_smaller(mid) >= k:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans
                
        