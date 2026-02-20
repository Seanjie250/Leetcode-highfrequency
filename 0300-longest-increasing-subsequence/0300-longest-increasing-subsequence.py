from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tail = []
        tail.append(nums[0])
        for num in nums[1:]:
            index = bisect_left(tail , num)
            if index >= len(tail):
                tail.append(num)
            else:
                tail[index] = num
           
        return len(tail)
        