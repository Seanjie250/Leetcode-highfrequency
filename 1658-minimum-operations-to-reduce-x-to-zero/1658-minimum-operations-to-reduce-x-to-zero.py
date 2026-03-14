class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        left = 0
        minm = float('inf')
        target = sum(nums) -  x
        cursum = 0
        for right , num in enumerate(nums):
            cursum += num
            while right >= left and cursum > target:
                cursum -= nums[left]
                left += 1
            if cursum == target:
                minm = min(minm , len(nums) - (right - left + 1))
        return minm if minm != float('inf') else  -1

        