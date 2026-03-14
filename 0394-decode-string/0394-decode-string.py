class Solution:
    def decodeString(self, s: str) -> str:
        num = 0
        stack = []
        i = 0
        string = ''
        for i in range(len(s)):
            ch = s[i]
            if ch.isdigit():
                num = num * 10 + int(ch)
                continue
            if ch == '[':
                stack.append((num , string))
                string = ''
                num = 0
            elif ch == ']':
                prenum , prestr = stack.pop()
                string = prestr + string * prenum
            else:
                string += ch
        return string
        