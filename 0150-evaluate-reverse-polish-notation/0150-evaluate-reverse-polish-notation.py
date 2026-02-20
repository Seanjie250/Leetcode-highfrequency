class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in '+-*/':
                val1 = stack.pop(-1)
                val2 = stack.pop(-1)
                if token == '+':
                    val3 = val1 + val2
                elif token == '-':
                    val3 = val2 - val1
                elif token == '*':
                    val3 = val2 * val1
                else:
                    val3 = int(val2 / val1)
                stack.append(val3)
            else:
                stack.append(int(token))
        return stack[-1]
        
        



        