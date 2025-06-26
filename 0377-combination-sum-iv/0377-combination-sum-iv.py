class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1,target + 1):
            for j in range(n):
                if i >= nums[j]:
                    dp[i] += dp[i - nums[j]]


        return dp[-1]
        