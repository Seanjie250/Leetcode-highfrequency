class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for word in wordDict:
            if s.startswith(word):
                dp[len(word)] = True
        for i in range(1 , len(s) + 1):
            for word in wordDict:
                j = len(word)
                if s[i - j:].startswith(word):
                    dp[i] = dp[i - j] or dp[i]
        return dp[len(s)]



        