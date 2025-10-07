class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        record = [0] * 26
        for char in s:
            record[ord(char) - ord('a')] += 1
        for char in t:
            record[ord(char) - ord('a')] -= 1
        for value in record:
            while value != 0:
                return False
        return True
            




