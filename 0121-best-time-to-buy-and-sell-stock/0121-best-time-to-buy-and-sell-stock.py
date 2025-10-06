class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * 2 for _ in range(n)]
        dp[0][0] = -prices[0]
        for i in range(1,len(prices)):
            dp[i][0] = max(dp[i - 1][0] , - prices[i])
            dp[i][1] = max(dp[i - 1][0] + prices[i] , dp[i - 1][1])
        return dp[n - 1][1]

            
