class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        target = sum(stones) // 2
        dp = [0] * (target + 1)
        # find the closest stone weight of half the sum
        for stone in stones:
            for j in range(target , stone - 1, -1):
                dp[j] = max(dp[j],dp[j - stone] + stone)
        return sum(stones) - 2*dp[target]
