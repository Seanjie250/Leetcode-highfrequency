class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        count = [1] * len(nums)
        m = 0
        if len(nums) == 1:
            return 1
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[j] < nums[i] and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    count[i] = count[j]
                elif dp[i] == dp[j] + 1:
                    count[i] += count[j]
            m = max(m , dp[i])
        return sum(c for l , c in zip(dp, count) if l == m)

        