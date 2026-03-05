class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        num = 0
        cur = ''
        for i in range(len(s)):
            ch = s[i]
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch == '[':
                stack.append((num , cur))
                num = 0
                cur = ''
            elif ch == ']':
                presum , prestr = stack.pop()
                cur = prestr + presum * cur 
            else:
                cur += ch
            print(cur)
        return cur

        