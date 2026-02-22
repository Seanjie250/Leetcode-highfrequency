class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        left , right = 0 , 0
        maxm = float('-inf')
        while right < len(s):
            count[s[right]] += 1
            maxlength = max(count.values())
            while right - left + 1 - maxlength > k:
                count[s[left]] -= 1
                left += 1
            maxm = max(maxm , right - left + 1)
            right += 1
        return maxm


        