# Last updated: 5/16/2025, 12:32:51 PM
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        record = 26 * [0]
        for i in s:
            record[ord(i)-ord('a')] += 1
        for j in t:
            record[ord(j)-ord('a')] -= 1
        for i in range(26):
            if record[i] != 0:
                return False
        return True

