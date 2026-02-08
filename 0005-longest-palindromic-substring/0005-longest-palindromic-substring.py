class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = 1
        l = len(s)
        start = 0
        dp = [[False for _ in range(l)] for _ in range(l)]
        for i in range(l):
            dp[i][i] = True
        
        for length in range(2 , l + 1):
            for i in range(0 , l - length + 1):
                j = i + length - 1

                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    if length == 2:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                if dp[i][j] and length > ans:
                    ans = max(ans , length)
                    start = i

        return s[start : start + ans ]
            
                    
                

                

        