class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        counter = {
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz'
        }
        def backtracking(path , i , rst):
            if len(path) == len(digits):
                rst.append(''.join(path))
            if i < len(digits):
                for ch in counter[digits[i]]:
                    path.append(ch)
                    backtracking(path , i + 1 , rst)
                    path.pop()

            return rst
        rst = backtracking([]  , 0 , [])
        return rst


        