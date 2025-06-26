class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [[0] * (target + 1) for _ in range(n)]
        for i in range(n):
            dp[i][0] = 1

        for j in range(1,target + 1):
            for i in range(n):
                if j < nums[i]:
                    dp[i][j] = dp[i - 1][j]
                else:
                
                    dp[i][j] = dp[i - 1][j] +  dp[-1][j - nums[i]]

        return dp[-1][-1]
        