class Solution:
    def __init__(self):
        self.lettermap = [
            "",
            "",
            "abc",
            "def",
            "ghi",
            "jkl",
            "mno",
            "pqrs",
            "tuv",
            "wxyz"
        ]
        self.result = []
        self.s = ""
    def backtracking(self,digits,index):
        if index == len(digits):
            self.result.append(self.s)
            return
        number = int(digits[index]) #locate the number
        letters = self.lettermap[number] # find the string 
        for i in range(len(letters)):
            self.s += letters[i]
            self.backtracking(digits,index + 1)
            self.s = self.s[:-1]
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        self.backtracking(digits,0)
        return self.result


        