class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        word_set = set(words)
        visited = set()
        rst = []
        def dfs(word):
            if word in word_set:
                return True
            if word in visited:
                return False
            for i in range(1,len(word)):
                pre , suf = word[:i] , word[i:]
                if pre in word_set:
                    if not dfs(suf):
                        visited.add(suf)
                    else:
                        return True
            return False
        
        for word in words:
            word_set.remove(word)
            if dfs(word):
                rst.append(word)
            word_set.add(word)
        return rst
                