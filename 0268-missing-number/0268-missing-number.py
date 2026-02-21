class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        rst = len(nums)
        for i in range(len(nums)):
            rst += i - nums[i]
        return rst
        


        