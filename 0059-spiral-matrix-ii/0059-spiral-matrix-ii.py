from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        rst = [[0] * n for _ in range(n)]
        val = 1
        offset = 0
        
        while val <= n * n:
            # left to right
            for i in range(offset, n - offset):
                rst[offset][i] = val
                val += 1

            # top to bottom
            for i in range(offset + 1, n - offset):
                rst[i][n - offset - 1] = val
                val += 1

            # right to left
            if val <= n * n:  # check to avoid duplicates
                for i in range(n - offset - 2, offset - 1, -1):
                    rst[n - offset - 1][i] = val
                    val += 1

            # bottom to top
            if val <= n * n:  # check to avoid duplicates
                for i in range(n - offset - 2, offset, -1):
                    rst[i][offset] = val
                    val += 1

            offset += 1
        
        return rst
