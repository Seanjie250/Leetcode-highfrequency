class Solution:
    def minWindow(self, s: str, t: str) -> str:
        have = 0
        
        hash_t = Counter(t)
        should_have = len(hash_t)
        hash_n = Counter()
        left , start = 0 , 0
        ans = float('inf')
        for right , x in enumerate(s):
            hash_n[x] += 1
            if x in hash_t and hash_n[x] == hash_t[x]:
                have += 1
            while have == should_have:
                if ans > right - left + 1:
                    ans = right - left + 1
                    start = left
                hash_n[s[left]] -= 1
                if s[left] in hash_t and hash_n[s[left]] < hash_t[s[left]]:
                    have -= 1
                left += 1

        return s[start : start + ans] if ans != float('inf') else ''