# Last updated: 5/12/2025, 3:59:35 PM
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        if len(nums) == 1:
            while nums[0] == target:
                return 0
            return -1
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] > target:
                right = middle - 1
            elif nums[middle] < target:
                left = middle + 1 
            else:
                return middle
        return -1



        