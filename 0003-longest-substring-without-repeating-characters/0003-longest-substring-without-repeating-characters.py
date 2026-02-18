class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left , right = 0 , 0
        max_length = 0
        n = len(s)
        count = defaultdict(int)
        while right <  n:
            if count[s[right]] == 0:
                count[s[right]] += 1
                max_length = max(max_length , right - left + 1)
                right += 1
            else:
                count[s[left]] -= 1
                left += 1
        return max_length

        


        