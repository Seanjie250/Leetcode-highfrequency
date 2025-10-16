class Solution:
    def reverseWords(self, s: str) -> str:
        word = s.split()
        reverse_word = word[::-1]
        return ' '.join(reverse_word)
        