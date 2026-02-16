class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        slow = 0 
        fast = 0
        count = 0
        while fast < len(nums):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
                count += 1
            fast += 1
        return count + 1

        
                
            
        