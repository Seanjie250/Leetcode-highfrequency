class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow , fast = 0 , 0
        count = 0 
        while fast < len(nums):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
                count += 1
            fast += 1
        return count
        