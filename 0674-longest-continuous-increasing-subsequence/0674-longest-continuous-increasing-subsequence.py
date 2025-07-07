class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        rst = 0
        dp  = [1] * len(nums)
        for i in range(1,len(nums)):
            if nums[i] > nums[i - 1]:
                dp[i] = dp[i - 1] + 1
            rst = max(rst,dp[i])
        return rst
            

        