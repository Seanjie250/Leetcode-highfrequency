# Last updated: 5/18/2025, 10:03:53 AM
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        record = [0]*26
        for char in magazine:
            record[ord(char)-ord('a')] += 1
        for char in ransomNote:
            key = ord(char) - ord('a')
            record[key] -= 1
            while record[key] < 0:
                return False
        return True        
        