class Solution:
    def decodeString(self, s: str) -> str:
        num = 0
        stack = []
        i = 0
        string = ''
        while i < len(s):
            ch = s[i]
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch == '[':
                stack.append((num , string))
                string = ''
                num = 0
            elif ch == ']':
                prenum , prestr = stack.pop()
                string = prestr + string * prenum
            else:
                string += ch
                print(string)
            i += 1
        return string
        