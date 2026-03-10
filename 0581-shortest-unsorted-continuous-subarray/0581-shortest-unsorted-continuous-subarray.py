class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < len(nums) - 1 and nums[left] <= nums[left + 1]:
                left += 1
        while right >= 0 and nums[right] >= nums[right - 1]:
                right -= 1 
        if left >= right:
            return 0
        
        maxm = max(nums[left : right + 1])
        minm = min(nums[left : right + 1])

        
        while left > 0 and nums[left - 1] > minm:
            left -= 1
        while right < len(nums) - 1 and nums[right + 1] < maxm:
            right += 1
               
    
        return right - left + 1

    


        