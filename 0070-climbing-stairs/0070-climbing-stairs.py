class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * ( n + 1 )
        if n == 1:
            return 1
        elif n == 2:
            return 2
        dp[0] = 0
        dp[1] = 1    
        for i in range(2 , n + 1):
            dp[i] = max(dp[i - 1] + 1 , dp[i - 2] + 1)
        return dp[-1]