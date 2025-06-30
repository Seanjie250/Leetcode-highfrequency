class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        left_profit = [0] * len(prices)
        right_profit = [0] * len(prices)

        min_price = prices[0]
        for i in range(1,len(prices)):
            min_price = min(prices[i],min_price)
            left_profit[i] = max(left_profit[i - 1],prices[i] - min_price)

        max_price = prices[-1]
        for i in range(len(prices) - 2,-1,-1):
            max_price = max(prices[i] , max_price)
            right_profit[i] = max(right_profit[i + 1],max_price - prices[i])

        max_profit = float('-inf')
        for i in range(len(prices)):
            max_profit = max(max_profit,right_profit[i] + left_profit[i])
        return max_profit
