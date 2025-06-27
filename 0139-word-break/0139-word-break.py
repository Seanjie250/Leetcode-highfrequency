class Solution:
    def backtracking(self,s,wordDict,startindex,memo):
        if startindex >= len(s):
            return True
        if startindex in memo:
            return False
        for i in range(startindex,len(s)):
            word = s[startindex:i + 1]
            if word in wordDict and self.backtracking(s,wordDict,i + 1,memo):
                return True
        memo.add(startindex)
        return False

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        memo = set()
        return self.backtracking(s,wordDict,0,memo)
