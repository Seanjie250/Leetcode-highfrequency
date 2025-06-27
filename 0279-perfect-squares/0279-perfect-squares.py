import numpy as np
class Solution:
    def numSquares(self, n: int) -> int:

        square = []
        for i in range(1,101):
            square.append(i * i)
        
        dp = [0] * (n + 1)
        dp[0] = 0
        for j in range(1,n+1):
            dp[j] = float('inf')
                    
        for i in range(round(np.sqrt(n))):
            for j in range(1,n+1):
                if j >= square[i]:
                    dp[j] = min(dp[j],(dp[j - square[i]] + 1))
        return dp[n]
        