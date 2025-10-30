class Solution:

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == '+':
                first = int(stack.pop())
                second = int(stack.pop())
                stack.append(second + first)
            elif token == '-':
                first = int(stack.pop())
                second = int(stack.pop())
                stack.append(second - first)
            elif token == '*':
                first = int(stack.pop())
                second = int(stack.pop())
                stack.append(second * first)
            elif token == '/':
                first = int(stack.pop())
                second = int(stack.pop())
                if second != 0:
                    stack.append(int(second / first))
                else:
                    stack.append(0)
            else:
                stack.append(int(token))
        return stack.pop()


        