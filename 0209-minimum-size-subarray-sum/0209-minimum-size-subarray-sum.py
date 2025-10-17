class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        length = float('inf')
        i ,j = 0, 0
        sum_ = 0
        for j in range(len(nums)):
            sum_ += nums[j]
            while sum_ >= target:
                sublength = j - i + 1
                length = min(length , sublength)
                sum_ -= nums[i]
                i += 1
        return length if length < float('inf') else 0

        

        

        