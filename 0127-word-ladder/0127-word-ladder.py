class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        q = deque()
        wordset = set(wordList)
        q.append(beginWord)
        count = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return count
                for j in range(26):
                    ch = chr(ord('a') + j)
                    for i in range(len(word)):
                        new_word = word[:i] + ch + word[i + 1:]
                        print(new_word)
                        if new_word in wordset:
                            wordset.remove(new_word)
                            q.append(new_word)
            count += 1
        return 0

                        
                    
        