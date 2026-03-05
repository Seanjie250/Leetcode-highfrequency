class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = {0 : 1}
        sum_ = 0
        rst = 0
        for num in nums:
            sum_ += num
            rst += prefix.get(sum_ - k ,0)
            prefix[sum_] = prefix.get(sum_ , 0) + 1
        return rst
            