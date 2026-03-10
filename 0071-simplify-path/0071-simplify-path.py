class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        print(path)
        stack = []
        for path in path:
            if path == '' or path == '.':
                continue
            elif path == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(path)
        return '/' + '/'.join(stack)

        