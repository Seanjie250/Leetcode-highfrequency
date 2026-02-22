class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        record = {0 : 1}
        prefix = 0
        ans = 0
        for num in nums:
            prefix += num
            ans += record.get(prefix - k , 0)
            print(ans)
            record[prefix] = record.get(prefix , 0) + 1
        return ans