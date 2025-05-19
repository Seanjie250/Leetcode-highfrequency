# Last updated: 5/19/2025, 3:06:07 PM
from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == '(':
                stack.append(')')
            elif char == '[':
                stack.append(']')
            elif char == '{':
                stack.append('}')
            elif not stack or stack[-1] != char:
                return False
            elif stack[-1] == char:
                stack.pop()
        return True if not stack else False
