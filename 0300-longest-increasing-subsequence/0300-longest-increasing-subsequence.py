from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tail = []

        for num in nums:
            i = bisect_left(tail , num)
            if i == len(tail):
                tail.append(num)
            else:
                tail[i] = num

        return len(tail)
