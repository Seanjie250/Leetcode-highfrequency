class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        count = 0
        freq = {0 : 1}
        for i in range(len(nums)):
            prefix_sum += nums[i]
            if prefix_sum -k in freq:
                count += freq[prefix_sum - k]
            freq[prefix_sum] = freq.get(prefix_sum , 0) + 1
        return count



        