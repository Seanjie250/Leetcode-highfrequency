class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        graph = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        rst = []
        path = []
        def dfs(i):
            if i == len(digits):
                rst.append(''.join(path))
                return
            for ch in graph[digits[i]]:
                path.append(ch)
                dfs(i + 1)
                path.pop()
        
        dfs(0)
        return rst

            
           
                

        