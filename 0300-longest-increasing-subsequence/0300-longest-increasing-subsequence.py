from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tail = []
        for num in nums:
            index = bisect_left(tail , num)
            if index == len(tail):
                tail.append(num)
            else:
                tail[index] = num
        return len(tail)
