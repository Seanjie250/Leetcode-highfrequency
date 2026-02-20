class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left  = 0
        count = 0
        fre = defaultdict(int)
        for right in range(len(s)):
            fre[s[right]] += 1
            maxlength = max(fre.values())
            length = right - left + 1
            if - maxlength + length > k:
                fre[s[left]] -= 1
                left += 1
            count = max(count , right - left + 1)
        return count
