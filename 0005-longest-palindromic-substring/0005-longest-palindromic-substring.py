class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxm = float('-inf')
        for i in range(len(s)):
            left , right = i , i
            while left >= 0  and right  < len(s) and s[left] == s[right] :
                left -= 1
                right += 1
            if right - left - 1 > maxm:
                start = left + 1
                maxm = right - left - 1
        for i in range(len(s)):
            left , right = i , i + 1
            while left  >= 0  and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            if right - left - 1 > maxm:
                start = left + 1
                maxm = right - left - 1
        return s[start : start + maxm]


        