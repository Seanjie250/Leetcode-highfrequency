class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m , n  = len(s1) , len(s2)
        if len(s1) + len(s2)  != len(s3):
            return False

        dp = [[False for _ in range(n + 1)] for _ in range(m + 1)]
        dp[0][0] = True

        for i in range(1, n + 1):
            if s2[i - 1] == s3[i - 1]:
                dp[0][i] = dp[0][i - 1]
        for i in range(1, m + 1):
            if s1[i - 1] == s3[i - 1]:
                dp[i][0] = dp[i -1][0]

        for j in range(1 , m + 1):
            for i in range(1 , n + 1):
                dp[j][i] = (dp[j - 1][i] and s1[j -1] == s3[i + j - 1]) or (dp[j][i - 1] and s2[i - 1] == s3[i + j - 1])

        return dp[m][n]
        
        