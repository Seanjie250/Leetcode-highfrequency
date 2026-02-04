class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = {}
        for i , a1 in enumerate(nums[1:] , start = 1):
            for j , a2 in enumerate(nums[:i]):
                d = nums[i] - nums[j]
                if (j , d) in dp:
                    dp[i , d] = dp[j , d] + 1
                else:
                    dp[i , d] = 2
        return max(dp.values())

        