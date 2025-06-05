class Solution:
    def ifpalindrome(self,s):
        return True if s == s[::-1] else False
    def backtracking(self,s,path,rst,startindex):
        if startindex == len(s):
            rst.append(path[:])
            return
        for i in range(startindex,len(s)):
            if self.ifpalindrome(s[startindex:i + 1]):
                path.append(s[startindex:i + 1])
                self.backtracking(s,path,rst,i+1)
                path.pop()
        
    def partition(self, s: str) -> List[List[str]]:
        rst = []
        path = []
        self.backtracking(s,path,rst,0)
        return rst
        