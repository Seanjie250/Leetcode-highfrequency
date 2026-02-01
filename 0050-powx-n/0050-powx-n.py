class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n < 0:
            x = 1 / x
            n = n * (- 1)

        rst = 1
        cur_product = x
        while n > 0:
            if n % 2 == 1:
                rst = rst * cur_product 
            cur_product = cur_product * cur_product
            n = n // 2
        return rst
        
        

        