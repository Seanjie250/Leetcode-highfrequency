class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        max_area = 0
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # keep your init style, but correct indices & string compare
        for i in range(1, m + 1):
            if matrix[i - 1][0] == "1":
                dp[i][1] = 1

        for j in range(1, n + 1):
            if matrix[0][j - 1] == "1":
                dp[1][j] = 1

        # dp transition (your structure preserved)
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if matrix[i - 1][j - 1] == "0":
                    dp[i][j] = 0
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) + 1
                max_area = max(max_area, dp[i][j])

        return max_area * max_area
