class Solution:
    def dp_(self, dp , n):
        if n <= 1:
            return 1
        if dp[n] != -1:
            return dp[n]
        ans = 0
        for i in range(1,  n + 1):
            ans += self.dp_(dp , n - i) * self.dp_(dp , i - 1)
        dp[n] = ans
        return dp[n]

    def numTrees(self, n: int) -> int:
        dp = [-1] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        return self.dp_(dp , n)