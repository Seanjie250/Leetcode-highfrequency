from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = Counter(t)
        l = 0
        rst = [-1, -1]
        have = 0
        need = len(t_count)
        minlength = float('inf')
        window_count = Counter()
        for r in range(len(s)):
            c = s[r]
            window_count[c] = window_count.get(c,0) + 1
            if c in t_count and t_count[c] == window_count[c]:
                have += 1
            while have == need:
                if (r - l + 1) < minlength:
                    minlength = r - l + 1
                    rst = [l , r]
                window_count[s[l]] -= 1
                if s[l] in t_count and t_count[s[l]] > window_count[s[l]]:
                    have -= 1
                l += 1
        l , r = rst
        return s[l : r + 1] if minlength != float('inf') else ""



            

        