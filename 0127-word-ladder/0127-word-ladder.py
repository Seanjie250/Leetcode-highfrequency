class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not endWord in wordList:
            return 0
        wordset = set(wordList)
        count = 1
        queue = deque([beginWord])
        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()
                for i in range(len(word)):
                    o_l = word[i]
                    for j in range(26):
                        n_l = chr(ord('a') + j)
                        n_word = word[:i ] + n_l + word[i + 1: ]
                        if n_word in wordset:
                            
                            print(count)
                            queue.append(n_word)
                            wordset.remove(n_word)
                        if n_word == endWord:
                            return count + 1
            count += 1
        return 0



