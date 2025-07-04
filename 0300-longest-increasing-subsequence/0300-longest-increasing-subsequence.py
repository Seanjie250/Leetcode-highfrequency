class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        rst = 0
        if len(nums) == 1:
            return 1
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i] , dp[j] + 1)
                if dp[i] > rst:
                    rst = dp[i]
                continue
        return rst
        
        