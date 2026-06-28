class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        count[0] = 1
        prefix = 0
        rst = 0
        for num in nums:
            prefix += num
            if prefix - k in count:
                rst += count[prefix - k]
            count[prefix] += 1
        return rst

        