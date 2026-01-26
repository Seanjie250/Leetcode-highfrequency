class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        rst = float('-inf')
        total = 0
        n = len(nums)
        
        cur_max = 0
        max_sum = nums[0]
        cur_min = 0
        min_sum = nums[0]

        for i in range(n):
            total += nums[i]

            cur_max = max(nums[i] , cur_max + nums[i])
            max_sum = max(max_sum , cur_max)

            cur_min = min(nums[i], cur_min + nums[i])
            min_sum = min(min_sum , cur_min)

        if max_sum < 0:
            return max_sum

        return max(max_sum , total - min_sum)

        

        
