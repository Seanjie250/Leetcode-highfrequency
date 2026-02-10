class Solution:
    def addBinary(self, a: str, b: str) -> str:
        rst = []
        left = 0
        total = 0
        i , j = len(a) - 1 , len(b) - 1
        while i >= 0 or j >= 0 or left == 1:
            total = left
            if i >= 0 :
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1
            rst.append(str(total % 2))
            left = total // 2
        
        return ''.join(rst[::-1])


        