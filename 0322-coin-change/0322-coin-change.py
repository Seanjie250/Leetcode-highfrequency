class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp = [float('inf')] * (amount + 1)
        for coin in coins:
            if coin <= amount:
                dp[coin] = 1
        for i in range(amount + 1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i - coin] + 1 , dp[i])
        print(dp)
        return dp[amount] if dp[amount] != float('inf') else - 1
        