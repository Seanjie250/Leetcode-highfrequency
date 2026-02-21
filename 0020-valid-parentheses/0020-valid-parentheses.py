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
                if not stack or stack.pop() != ch:
                    return False
            if ch == ']':
                if not stack or stack.pop() != ch:
                    return False
            if ch == '}':
                if not stack or stack.pop() != ch:
                    return False
        return True if not stack else False
                   

            