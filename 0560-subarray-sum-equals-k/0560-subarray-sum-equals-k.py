class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        record = {0 : 1}
        prefix = 0
        rst = 0
        for num in nums:
            prefix += num
            rst += record.get(prefix - k , 0)
            record[prefix] = record.get(prefix , 0) + 1
        return rst 
        