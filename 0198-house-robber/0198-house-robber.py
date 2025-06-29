class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums)

        dp = [0] * (len(nums) + 1)
        dp[0] = 0
        dp[1] = nums[0]
        dp[2] = nums[1] if nums[1] >= nums[0] else nums[0]
        for j in range(3,len(nums) + 1):
            dp[j] = max(dp[j - 1],dp[j-2] + nums[j - 1])
        return dp[len(nums)]
        