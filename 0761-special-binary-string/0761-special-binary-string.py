class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        def solve(s):
            if len(s) <= 2:
                return s
            start = 0 
            count = 0
            part = []
            for idx , ch in enumerate(s):
                if ch == '1':
                    count += 1
                else:
                    count -= 1
                if count == 0:
                    inner = solve(s[start + 1 : idx])
                    part.append('1' + inner + '0')
                    start = idx + 1
            part.sort(reverse = True)
            return ''.join(part)
        return solve(s)
                    