class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        root = x // 2

        while root * root > x :
            root = (root + x // root) // 2
        
        return root
        