class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        rst = float('-inf')
        count = 0
        for i in range(len(nums)):
            count += nums[i]

            if count > rst:
                rst = count
            if count < 0:
                count = 0
        return rst
            

        