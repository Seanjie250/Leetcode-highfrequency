class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch == '(':
                stack.append(')')
            if ch == '[':
                stack.append(']')
            if ch == '{':
                stack.append('}')
            if ch == ')':
                if not stack or ch != stack.pop():
                    return False
            if ch == ']':
                if not stack or ch != stack.pop():
                    return False
            if ch == '}':
                if not stack or ch != stack.pop():
                    return False
        return True if not stack else False