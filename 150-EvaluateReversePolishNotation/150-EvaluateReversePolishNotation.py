# Last updated: 5/19/2025, 3:47:06 PM
from operator import add, sub, mul
def div(x:int,y:int) -> int:
    return int(x/y) if x * y > 0 else -(abs(x)//abs(y))

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        self.op_map = {
            '+' : add,
            '-' : sub,
            '*' : mul,
            '/' : div
        }
        for char in tokens:
            if char not in {'+','-','*','/'}:
                stack.append(int(char))
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(self.op_map[char](op1,op2))
        return stack.pop()

        