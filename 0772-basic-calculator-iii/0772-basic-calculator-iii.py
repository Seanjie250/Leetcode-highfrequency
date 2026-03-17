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

                if ch == ')':
                    break

                # operator
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack[-1] *= num
                elif sign == '/':
                    stack[-1] = int(stack[-1] / num)

                sign = ch
                num = 0
                i += 1

            if sign == '+':
                stack.append(num)
            elif sign == '-':
                stack.append(-num)
            elif sign == '*':
                stack[-1] *= num
            elif sign == '/':
                stack[-1] = int(stack[-1] / num)

            i += 1  # move past ')'
            return sum(stack)

        return helper()