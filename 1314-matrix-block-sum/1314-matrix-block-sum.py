class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m , n = len(mat) , len(mat[0])
        rst = [[0] * n for _ in range(m)]
        def blocksum(i , j):
            s = 0
            for r in range(max(0 , i - k) , min(i + k + 1 , m)):
                for c in range(max(0 , j - k) , min(j + k + 1 , n)):
                    s += mat[r][c]
            return s
        for i in range(m):
            for j in range(n):
                rst[i][j] = blocksum(i , j)
        return rst
        