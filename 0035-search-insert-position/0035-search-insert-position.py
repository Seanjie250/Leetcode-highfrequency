class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        index = 0
        if target in nums:
            for i in range(len(nums)):
                if nums[i] == target:
                    return i
        elif target not in nums and target < nums[-1]:
            for i in range(len(nums)):
                if nums[i] > target:
                    return i
        elif  target > nums[-1]:
            return len(nums)

        