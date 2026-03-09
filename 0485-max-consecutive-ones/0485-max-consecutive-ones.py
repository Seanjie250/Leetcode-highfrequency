class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        maxm = 0
        n = len(nums)
        i = 0
        while i < n:
            if nums[i] == 1:
                count += 1
                maxm = max(count , maxm)
            else:
                count = 0
            i += 1
        return maxm
            
        