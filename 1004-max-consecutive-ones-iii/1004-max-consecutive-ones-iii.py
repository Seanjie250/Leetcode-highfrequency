class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        maxm = 0
        zerocount = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zerocount += 1
            while zerocount > k:
                if nums[left] == 0:
                    zerocount -= 1
                left += 1
            maxm = max(maxm , right - left + 1)
        return maxm




        