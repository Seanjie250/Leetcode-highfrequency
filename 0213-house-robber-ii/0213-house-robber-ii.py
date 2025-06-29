class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        nums_1 = nums[1:]
        nums_2 = nums[:-1]
        return max(self.robbing(nums_1),self.robbing(nums_2))

    def robbing(self,nums):
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        dp = [0]  * (len(nums) + 1)
        dp[0] = 0
        dp[1] = nums[0]
        dp[2] = max(nums[1],nums[0])
        for i in range(3,len(nums) + 1):
            dp[i] = max(dp[i - 1],dp[i - 2] + nums[i -1])
        return dp[len(nums)]
        