from bisect import bisect_left
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        prefix_sum_balance = Counter([0])
        balance = 0
        ans = 0
        found = False
        for num in nums:
            if num > k:
                balance += 1
            elif num < k:
                balance -= 1
            else:
                found = True
            if found:
                ans += prefix_sum_balance[balance - 1] + prefix_sum_balance[balance]
            else:
                prefix_sum_balance[balance] += 1
        return ans


        