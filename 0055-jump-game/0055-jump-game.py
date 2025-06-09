class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cover = 0
        if len(nums) == 1:
            return True
        i = 0
        while i <= cover:
            cover = max(nums[i] + i,cover)
            if cover >= len(nums) - 1:
                return True
            i += 1
        return False