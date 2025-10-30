class Solution:
    def simplifyPath(self, path: str) -> str:
        output = []
        parts = path.split("/")
        rst = []
        for part in parts:
            if part == '.' or part == '':
                continue
            elif part == '..':
                if output:
                    output.pop()
            else:
                output.append(part)
        return '/' + '/'.join(output)
       