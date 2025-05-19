# Last updated: 5/19/2025, 3:21:28 PM
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        if len(s) == 1:
            return s
        for char in s:
            if not stack:
                stack.append(char)
            elif char != stack[-1]:
                stack.append(char)
            else:
                stack.pop()
        return ''.join(stack)

        