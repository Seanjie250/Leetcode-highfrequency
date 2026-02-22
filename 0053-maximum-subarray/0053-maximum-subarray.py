class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        maxm = float('-inf')
        prefix = 0
        for num in nums:
            if prefix <= 0:
                prefix = 0
            prefix += num
            maxm = max(maxm , prefix)
        return maxm

        