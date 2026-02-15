class Solution:
    def calculate_(self, s , start , end , rightpair) -> int:
        stack = []
        num = 0
        i = start
        pre_op = '+'
        while i <= end:
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            elif s[i] == '(':
                num = self.calculate_(s , i + 1 , rightpair[i] - 1 , rightpair)
                i = rightpair[i]
            if s[i] in '+-/*' or i == end:
                if pre_op == '+':
                    stack.append(num)
                elif pre_op == '-':
                    stack.append(-num)
                elif pre_op == '/':
                    stack.append(math.trunc(stack.pop() / num))
                elif pre_op == '*':
                    stack.append(stack.pop() * num)
                num = 0
                pre_op = s[i]
            i += 1
        return sum(stack)
    def calculate(self, s:str) -> int:
        rightpair = {}
        stack = []
        for i,ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            elif ch == ')':
                rightpair[stack.pop()] = i
        
        return self.calculate_(s, 0 , len(s) - 1 , rightpair)

