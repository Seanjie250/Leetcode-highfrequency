class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = {0 : 1}
        prefix = 0
        ans = 0
        for num in nums:
            prefix += num
            ans += count.get(prefix - k , 0)
            count[prefix] = count.get(prefix , 0) + 1
            
        return ans

        