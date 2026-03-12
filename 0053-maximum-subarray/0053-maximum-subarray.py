class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prefix_sum = 0
        minm_prefix = 0
        ans = float('-inf')
        for num in nums:
            prefix_sum += num
            ans = max(ans , prefix_sum - minm_prefix)
            minm_prefix = min(prefix_sum , minm_prefix)
        return ans        