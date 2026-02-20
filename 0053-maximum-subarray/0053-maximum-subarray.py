class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        maxm = float('-inf')
        total = 0
        for num in nums:
            if total <= 0:
                total = 0
            total += num
            maxm = max(maxm , total)
        return maxm
        