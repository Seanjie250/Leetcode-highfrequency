class Solution:
    def is_valid(self, s, start, end):
        if start > end:
            return False
        if s[start] == '0' and start != end: 
            return False
        num = 0
        for i in range(start, end + 1):
            if not s[i].isdigit():  
                return False
            num = num * 10 + int(s[i])
            if num > 255: 
                return False
        return True
    def backtracking(self,s,points,current,rst,startindex):
        if points == 3:
            if self.is_valid(s,startindex,len(s) - 1):
                current += s[startindex:]
                rst.append(current)
                return 
        for i in range(startindex , len(s)):
            if self.is_valid(s,startindex,i):
                sub = s[startindex : i + 1]
                self.backtracking(s,points + 1,current + sub + '.',rst,i + 1)
            else:
                 break
    def restoreIpAddresses(self, s: str) -> List[str]:
        rst = []
        self.backtracking(s,0,'',rst,0)
        return rst

        