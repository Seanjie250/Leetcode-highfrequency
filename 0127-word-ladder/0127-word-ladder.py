class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        wordListset = set(wordList)
        visited = set([beginWord])
        q = deque()
        q.append(beginWord)
        count = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                word = list(word)
                for j in range(len(word)):  
                    original = word[j]
                    for k in range(26):
                        
                        word[j] = chr(ord('a') + k)
                        new_word = ''.join(word)
                        print(new_word)
                        if new_word == endWord:
                            return count + 1
                        if new_word in wordListset and new_word not in visited:
                            visited.add(new_word)
                            q.append(new_word)
            
                            print(count)
                    word[j] = original
            count += 1
        return 0    
                    

                    



        
