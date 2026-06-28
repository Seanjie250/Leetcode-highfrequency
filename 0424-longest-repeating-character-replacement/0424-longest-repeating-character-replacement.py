class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        maxm = 0
        rst  = 0
        table = defaultdict(int)
        for r in range(len(s)):
            letter = s[r]
            table[letter] += 1
            maxm = max(maxm , table[letter])
            while r - l + 1 - maxm > k:
                table[s[l]] -= 1
                if table[s[l]] == 0:
                    del table[s[l]]
                l += 1
            rst = max(rst , r - l + 1)
        return rst

