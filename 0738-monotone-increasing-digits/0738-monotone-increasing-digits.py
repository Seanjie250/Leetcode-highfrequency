class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        str_n = list(str(n))
        flag = 0
        for i in range(len(str_n) - 1,0,-1):
            if str_n[i - 1] > str_n[i]:
                str_n[i -1] = str(int(str_n[i-1]) - 1)
                for j in range(i,len(str_n)):
                    str_n[j] = '9'
        return int(''.join(str_n))

        
        
        