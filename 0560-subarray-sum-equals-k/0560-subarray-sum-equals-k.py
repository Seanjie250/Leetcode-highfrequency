class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = 0
        count = defaultdict(int)
        count[0] = 1
        rst = 0
        for num in nums:
            prefix += num
            rst += count.get(prefix - k , 0) 
            count[prefix] += 1
        return rst
        