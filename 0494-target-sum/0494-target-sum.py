class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if (target + sum(nums)) % 2 == 1 or abs(target) > sum(nums):
            return 0
        sum_left = (target + sum(nums)) // 2

        dp = [[0] * (sum_left + 1) for _ in range(len(nums) + 1)]

        dp[0][0] = 1

        for i in range(1,len(nums) + 1):
            for j in range(sum_left + 1):
                if nums[i - 1] > j:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i-1][j - nums[i - 1]]
                
        return dp[len(nums)][sum_left]


        