class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0] , nums[1])
        n = len(nums)
        dp = [0] * (n + 1)
        dp[1] = nums[0]
        dp[2] = max(nums[1] , nums[0])
        for i in range(3 , n + 1):
            dp[i] = max(dp[i - 1] , dp[i - 2] + nums[i - 1])
        return max(dp)