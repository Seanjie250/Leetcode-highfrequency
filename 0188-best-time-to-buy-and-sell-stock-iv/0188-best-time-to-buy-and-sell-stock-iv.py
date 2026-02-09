class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices) # days
        dp = [[[0] * 2  for _ in range(k + 1)] for _ in range(n)]
        for i in range(1, k + 1):
            dp[0][i][1] = -prices[0]
        
        for i in range(1, n ):
            for j in range(1, k + 1):
                dp[i][j][0] = max(prices[i] + dp[i - 1][j][1] , dp[i - 1][j][0])
                dp[i][j][1] = max(dp[i - 1][j][1] , dp[i - 1][j - 1][0] - prices[i])
        return dp[-1][-1][0]





        