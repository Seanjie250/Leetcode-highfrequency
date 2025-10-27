from typing import List
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        rst = []
        start = 0
        while start < len(nums):
            end = start
            while end < len(nums) - 1 and nums[end + 1] == nums[end] + 1:
                end += 1
            if end == start:
                rst.append(str(nums[start]))
            else:
                rst.append(f"{nums[start]}->{nums[end]}")
            start = end + 1
        return rst
            

        
        