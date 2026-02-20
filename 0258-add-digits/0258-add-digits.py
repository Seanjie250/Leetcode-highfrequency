class Solution:
    def addDigits(self, num: int) -> int:
        rst = 0
        while True:
            if num < 10:
                return num
            while num > 0:
                rst += num % 10
                num = num // 10
            num = rst
            rst = 0
            

        


            
        
        