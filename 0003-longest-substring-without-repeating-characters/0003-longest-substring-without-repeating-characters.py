class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        maxm = float('-inf')
        count = defaultdict(int)
        if not s:
            return 0
        for right in range(len(s)):
            ch = s[right]
            count[ch] += 1
            while count[ch] > 1:
                count[s[left]] -= 1
                left += 1
           
            maxm = max((right - left + 1) , maxm)
        return maxm

        