class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        need = Counter(p)
        window = Counter()
        left , right = 0 , 0 
        rst = []
        valid = 0
        while right < len(s):
            ch = s[right]
            right += 1
            if ch in need:
                window[ch] += 1
                if window[ch] == need[ch]:
                    valid += 1
            while right - left >= len(p):
                if valid == len(need):
                    rst.append(left)
                d = s[left]
                left += 1
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        return rst 
        