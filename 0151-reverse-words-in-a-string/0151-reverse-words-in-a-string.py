class Solution:
    def reverseWords(self, s: str) -> str:
        s = " ".join(s.split())  
        print (s)
        s = list(s)
        s.reverse()
        n = len(s)
        start = 0
        for i in range(n + 1):
            if i == n or s[i] == ' ':
                l , r = start , i - 1
                while l < r:
                    s[l] , s[r] = s[r] , s[l]
                    l += 1
                    r -= 1
                start = i + 1
        return ''.join(s)


        