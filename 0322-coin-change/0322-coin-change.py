class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 0
        for j in range(1,amount + 1):
            dp[j] = float('inf')
        for i in range(len(coins)):
            for j in range(1,amount + 1):
                if j >= coins[i]:
                    dp[j] = min(dp[j] , (dp[j - coins[i]] + 1))
        if dp[amount] < float('inf'):
            return dp[amount]
        else:
            return -1

        

        