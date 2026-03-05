class Solution:
    def calculate(self, s: str) -> int:
        i = 0
        def helper():
            n = len(s)
            nonlocal i
            stack = []
            sign = '+'
            num = 0
            while i < n:
                ch = s[i]
                if ch == ' ':
                    i += 1
                    continue
                if ch.isdigit():
                    num = num * 10 + int(ch)
                    i += 1
                    continue
                if ch == '(':
                    i += 1
                    num = helper()
                    continue
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack[-1] = stack[-1] * num
                elif sign == '/':
                    stack[-1] = int(stack[-1] / num)
                if ch == ')':
                    i += 1
                    return sum(stack)
                num = 0
                sign = ch 
                i += 1

            if sign == '+':
                stack.append(num)
            elif sign == '-':
                stack.append(-num)
            elif sign == '*':
                stack[-1] = stack[-1] * num
            elif sign == '/':
                stack[-1] = int(stack[-1] / num)
            return sum(stack)
        return helper()
                

            
        

        