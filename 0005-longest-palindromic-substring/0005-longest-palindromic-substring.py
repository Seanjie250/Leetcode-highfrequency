class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ''
        def expandfromcenter(s , left , right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                right += 1
                left -= 1
            return right - left - 1
        
        start = 0
        end = 0

        for i in range(len(s)):
            odd = expandfromcenter(s, i , i)
            even = expandfromcenter(s, i , i + 1)
            maxm = max(odd ,even)

            if maxm > end - start:
                start = i - (maxm - 1) // 2
                end = i + maxm // 2

        return s[start : end + 1]        