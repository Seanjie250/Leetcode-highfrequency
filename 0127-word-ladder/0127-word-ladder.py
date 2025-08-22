class Solution:
    def checkletter(self,before:str,after:str):
        diff = 0
        for a,b in zip(before,after):
            if a != b:
                diff += 1
            if diff > 1:
                return False
        return diff == 1

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord == endWord:
            return 0
        if not endWord in wordList:
            return 0
        n = len(wordList)
        visited = [False for _ in range(n)]
        queue = [[beginWord,1]]
        while queue:
            string,step = queue.pop(0)
            if self.checkletter(string,endWord):
                return step + 1
            for i in range(n):
                if not visited[i] and self.checkletter(string,wordList[i]):
                    visited[i] = True
                    queue.append([wordList[i],step + 1])
        return 0
        
        
        


            
            
        
