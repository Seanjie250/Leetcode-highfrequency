class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        cover = 0
        i = 0
        while i <= cover:
            cover = max(cover , nums[i] + i)
            if cover >= len(nums) - 1:
                return True
            i += 1
        return False
            
