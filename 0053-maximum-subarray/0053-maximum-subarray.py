class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxm = nums[0]
        cur = nums[0]
        for num in nums[1:]:
            cur = max(num , cur + num)
            maxm = max(cur , maxm)
        return maxm
        