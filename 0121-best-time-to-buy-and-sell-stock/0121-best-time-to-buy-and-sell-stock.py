class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = [[0] * 2 for _ in range(len(prices))]
        profit[0][0] = -prices[0]
        profit[0][1] = 0
        for i in range(1,len(prices)):
            profit[i][0] = max(-prices[i] , profit[i - 1][0])
            profit[i][1] = max(profit[i - 1][1] , prices[i] + profit[i - 1][0])
        return profit[len(prices) - 1][1]        
        


            
