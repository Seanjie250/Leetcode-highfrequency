class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        seen = set()
        for left in range(len(s) - k + 1):
            
            if s[left:left + k] not in seen:
                seen.add(s[left:left + k])
        print(seen)
        return len(seen) == 2 ** k