class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = Counter(nums)
        for num , counts in count.items():
            if counts == 1:
                return num
