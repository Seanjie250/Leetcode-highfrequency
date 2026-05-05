class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def is_valid(s):
            stack = []
            for ch in s:
                if ch == '(':
                    stack.append(ch)
                elif ch == ')':
                    if not stack:
                        return False
                    else:
                        stack.pop()
            return True if not stack else False
        
        visited = {s}
        queue = deque([s])

        while queue:
            level_length = len(queue)
            rst = []
            for _ in range(level_length):
                cur = queue.popleft()
                if is_valid(cur):
                    rst.append(cur)
                    continue
                for i in range(len(cur)):
                    nxt = cur[:i] + cur[i + 1 : ]

                    if nxt not in visited:
                        visited.add(nxt)
                        queue.append(nxt)
            if rst:
                return rst
        return [""]            

            
                

        