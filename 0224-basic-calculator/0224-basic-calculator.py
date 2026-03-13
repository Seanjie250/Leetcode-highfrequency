class Solution:
    def calculate(self, s: str) -> int:
        i = 0
        
        def helper():
            nonlocal i
            stack = []
            num = 0
            sign = '+'
            while i < len(s):
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
                    num = 0
                elif sign == '-':
                    stack.append(-num)
                    num = 0
                elif sign == '*':
                    stack[-1] = (stack[-1] * num)
                    num = 0
                elif sign == '/':
                    stack[-1] = (stack[-1] // num)
                    num = 0
                if ch == ')':
                    i += 1
                    return sum(stack)
                i += 1
                sign = ch
                
            if sign == '+':
                stack.append(num)    
            elif sign == '-':
                stack.append(-num)
            elif sign == '*':
                stack[-1] = (stack[-1] * num)
            elif sign == '/':
                stack[-1] = (stack[-1] // num)
            return sum(stack)
        return helper()
                



