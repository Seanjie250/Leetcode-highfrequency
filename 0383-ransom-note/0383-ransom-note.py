from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
             counter_ransom = Counter(ransomNote)
             counter_magazine = Counter(magazine)
             for ch , val in counter_ransom.items():
                if counter_magazine[ch] < val:
                    return False
             return True
        