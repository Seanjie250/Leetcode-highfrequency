class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxm = 0
        numset = set(nums)
        for num in nums:
            if num - 1 not in numset:
                count = 1
                cur = num
                while cur + 1 in numset:
                    count += 1
                    cur += 1
                maxm = max(maxm , count)
        return maxm
                
                
        