from collections import Counter
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return None
        
        word_len = len(words[0])
        total_len = word_len * len(words)
        word = Counter(words)
        rst = []

        for i in range(word_len):
            left = i
            seen = Counter()
            for j in range(i , len(s) - word_len + 1 , word_len):
                next_word = s[j : j + word_len]
                if next_word in word:
                    seen[next_word] += 1
                    while seen[next_word] > word[next_word]:
                        seen[s[left:left + word_len]] -= 1
                        left += word_len
                    if j - left + word_len == total_len:
                        rst.append(left)
                else:
                    seen.clear()
                    left = j + word_len
        return rst
        


                
            

        