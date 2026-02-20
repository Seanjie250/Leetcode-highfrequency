class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = Counter(s)
        for ch , cot in count.items():
            if cot == 1:
                index = s.find(ch)
                return index 
        return -1