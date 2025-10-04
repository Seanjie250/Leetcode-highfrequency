class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i ,j = 0 , 0
        sum = 0
        rst = float('inf')
        for j in range(len(nums)):
            sum += nums[j]
            while (sum >= target):
                sublength = (j - i + 1)
                rst = min(rst,sublength)
                sum -= nums[i]
                i += 1
        return rst if rst < float('inf') else 0

        

        

        