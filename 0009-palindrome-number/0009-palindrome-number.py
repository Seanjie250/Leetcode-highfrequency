class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        x = list(x)
        return x == x[::-1]