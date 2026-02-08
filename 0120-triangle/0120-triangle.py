class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = []
        if len(triangle) == 1:
            return triangle[0][0]
        if len(triangle) == 2:
            return triangle[0][0] + min(triangle[1][0] , triangle[1][1])
        for list_ in triangle:
            rst = [0] * len(list_)
            dp.append(rst)
        
        dp[0][0] = triangle[0][0]
        for i in range(1,len(triangle)):
            dp[i][0] = dp[i - 1][0] + triangle[i][0]
            dp[i][i] = dp[i - 1][i - 1] + triangle[i][i]

        for i in range(2,len(triangle)):
            for j in range(1, i):
                dp[i][j] = min(dp[i - 1][j] , dp[i - 1][j - 1]) + triangle[i][j]
        
        return min(dp[len(triangle) - 1])

            

        