class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp = [-1] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            if coin <= amount:
                dp[coin] = 1
        for i in range(1, (amount + 1)):
            for coin in coins:
                if i >= coin and dp[i - coin] > -1 and dp[i] > -1:
                    dp[i] = min(dp[i - coin] + 1 , dp[i])
                elif i >= coin and dp[i - coin] > -1 and dp[i] == -1:
                    dp[i] = dp[i - coin] + 1
                
        return dp[amount]


        

        