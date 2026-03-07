class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxm = float('-inf')
        start = 0
        for i in range(len(s)):
            left , right = i , i
            while left >= 0 and right < len(s) and s[left] == s[right]:   
                if right - left + 1 > maxm:
                    maxm = right - left + 1
                    start = left
                left -= 1
                right += 1
        for i in range(len(s)):
            left , right = i , i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:   
                if right - left + 1 > maxm:
                    maxm = right - left + 1
                    start = left
                left -= 1
                right += 1
        return s[start : start + maxm]


        