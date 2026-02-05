class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)

        index = {}

        for i in range(len(arr)):
            index[arr[i]] = i
        
        dp = [[2] * n for _ in range(n)]

        rst = 0

        for i in range(len(arr)):
            for j in range(i):
                prev = arr[i] - arr[j]
                if prev in index and index[prev] < j:
                    k = index[prev]
                    dp[j][i] = dp[k][j] + 1
                rst = max(rst , dp[j][i])
        return rst if rst >= 3 else 0
                


