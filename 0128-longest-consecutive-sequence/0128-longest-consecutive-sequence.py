class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        num_set = set(nums)
        max_length = float('-inf')
        for num in num_set:
            if num - 1 not in num_set:
                cur = num
                length = 1
                while cur + 1 in num_set:
                    cur = cur + 1
                    length += 1
                max_length = max(max_length , length)
        return max_length
        