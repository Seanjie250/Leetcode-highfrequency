class Solution:
    def get_sum(self,n):
        sum = 0
        while n > 0:
            sum += (n % 10)** 2 
            n = n // 10
        return sum
    def isHappy(self, n: int) -> bool:
        record = set()
        while n != 1 and n not in record:
            record.add(n)
            n = self.get_sum(n)
        return n == 1


        