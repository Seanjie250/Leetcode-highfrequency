# Last updated: 5/19/2025, 10:17:42 AM
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        head = 0 
        tail = len(s) - 1
        while head < tail:
            s[head],s[tail] = s[tail],s[head]
            head += 1
            tail -= 1
        
        