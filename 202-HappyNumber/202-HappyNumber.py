# Last updated: 5/17/2025, 4:43:16 PM
class Solution:
    def isHappy(self, n: int) -> bool:
        record = set()
        while True:
            n = self.get_sum(n)
            if n == 1:
                return True
            if n in record:
                return False
            else:
                record.add(n)
            
        
    def get_sum(self, n:int) -> int:
        sum = 0
        while n:
            n ,r = divmod(n,10)
            sum += r**2
        return sum