# Last updated: 5/13/2025, 3:57:04 PM
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l , r ,total = 0 ,0 ,0
        lenth = float('inf')
        while r < len(nums):
            total += nums[r]
            while total >= target:
                lenth = min(lenth,(r - l +1))
                total -= nums[l]
                l += 1
            r += 1
        
           
        return lenth if lenth < float('inf') else 0

        

        