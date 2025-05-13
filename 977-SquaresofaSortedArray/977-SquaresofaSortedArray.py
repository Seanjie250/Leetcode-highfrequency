# Last updated: 5/13/2025, 3:25:51 PM
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(0,len(nums)):
            nums[i] = nums[i] * nums[i]
        nums.sort()
        return nums


        