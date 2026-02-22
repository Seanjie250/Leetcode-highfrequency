class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordset = set(wordList)
        if endWord not in wordset:
            return 0
        q = deque()
        q.append(beginWord)
        count = 1
        while q:
            for k in range(len(q)):
                cur = q.popleft()
                word = list(cur)
                for i in range(len(word)):
                    original = word[i]
                    for j in range(26):
                        word[i] = chr(ord('a') + j)
                        new_word = ''.join(word)
                        if new_word == endWord:
                            return count + 1
                        if new_word in wordset:
                            q.append(new_word)
                            wordset.remove(new_word)
                    word[i] = original
            count += 1
        
        return 0


        