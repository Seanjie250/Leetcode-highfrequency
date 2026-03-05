from math import gcd
class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        if x + y < target:
            return False
        if target == 0:
            return True
        return target % gcd(x , y) == 0
        
        


