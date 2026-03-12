class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur  , ans = nums[0] , nums[0]
        for num in nums[1:]:
            cur = max(num , cur + num)    
            ans = max(ans , cur)
        return ans