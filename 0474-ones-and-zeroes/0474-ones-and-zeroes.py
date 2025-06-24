class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)] 

        for s in strs:
            zeronum = s.count('0')
            onenum = len(s) - zeronum
            for i in range(m,zeronum -1,-1):
                for j in range(n,onenum-1,-1):
                    dp[i][j] = max(dp[i][j],dp[i - zeronum][j - onenum] + 1)

        return dp[m][n]