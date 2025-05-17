# Last updated: 5/17/2025, 10:13:51 AM
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if not words:
            return []
        hash1 = [0]*26
        result = []
        for i,ch in enumerate(words[0]):
            hash1[ord(ch) - ord('a')] += 1
        for i in range(1,len(words)):
            hash2 = [0]*26
            for j in range(len(words[i])):
                hash2[ord(words[i][j]) - ord('a')] += 1
            for k in range(26):
                hash1[k] = min(hash1[k],hash2[k])
        for i in range(26):
            while hash1[i] != 0:
                for _ in range(hash1[i]):
                    result.extend(chr(i + 97))
                    hash1[i] -= 1
        return result 

        


        