from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch == '(':
                stack.append(')')
            elif ch == '{':
                stack.append('}')
            elif ch == '[':
                stack.append(']')
            elif not stack or stack[- 1] != ch:
                return False
            elif stack[-1] == ch:
                stack.pop()
        return True if not stack else False
                