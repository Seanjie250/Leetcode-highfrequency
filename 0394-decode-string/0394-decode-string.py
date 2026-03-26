class Solution:
    def decodeString(self, s: str) -> str:
        ans = ''
        
        num = 0
        stack = []
        for i in range(len(s)):
            ch = s[i]
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch == '[':
                stack.append((ans  , num))
                ans = ''
                num = 0
            elif ch == ']':
                prev_str, k = stack.pop()
                ans = prev_str + k * ans
            else:
                ans += ch
        return ans