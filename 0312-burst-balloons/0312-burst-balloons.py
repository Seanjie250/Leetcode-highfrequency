class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * len(nums) for _ in range(len(nums))]
        for length in range(2 , n):
            for l in range(n - length):
                r = l + length
                best = 0
                for k in range(l + 1 , r):
                    best = max(best , dp[l][k] + nums[r] * nums[k] * nums[l] + dp[k][r])
                dp[l][r] = best
                print(best)
        return dp[0][n - 1]

                
        