class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        rst = 0
        num = 0
        sign = 1
        i = 0
        n = len(s)

        while i < n:
            ch = s[i]
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch in ['+', '-']:
                rst += sign * num
                num = 0
                sign = 1 if ch == '+' else -1
            elif ch == '(':
                # push current result and sign
                stack.append(rst)
                stack.append(sign)
                # reset result and sign for inner expression
                rst = 0
                sign = 1
            elif ch == ')':
                rst += sign * num
                num = 0
                sign = stack.pop()  # sign before '('
                prev_rst = stack.pop()  # result before '('
                rst = prev_rst + sign * rst
            i += 1
        return rst + sign * num
