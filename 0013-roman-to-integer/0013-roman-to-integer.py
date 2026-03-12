class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
            }
        rst = 0
        for i in range(len(s)):
            if i + 1 < len(s) and mapping[s[i]] < mapping[s[i + 1]]:
                rst -= mapping[s[i]]
            else:
                rst += mapping[s[i]]
        return rst
        