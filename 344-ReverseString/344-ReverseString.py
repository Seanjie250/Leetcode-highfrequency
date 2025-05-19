# Last updated: 5/19/2025, 10:25:29 AM
class Solution:
    def reverseWords(self, s: str) -> str:
        word = s.split()
        reverser_word = word[::-1]
        return " ".join(reverser_word)
        