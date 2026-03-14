class Difference:
    def __init__(self , nums):
        self.diff = [0] * len(nums)
        self.diff[0] = nums[0]
        for i in range(1,len(nums)):
            self.diff[i] = nums[i] - nums[i - 1]
       
    def increase(self , val , i , j):
        self.diff[i] += val
        if j + 1 < len(self.diff):
            self.diff[j + 1] -= val

    def rst(self):
        rst = [0] * len(self.diff)
        rst[0] = self.diff[0]
        for i in range(1 , len(self.diff)):
            rst[i] = rst[i - 1] + self.diff[i]
        return rst

class Solution:
    
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        num = [0] * n
        DF = Difference(num)
        for booking in bookings:
            i = booking[0] - 1
            j = booking[1] - 1
            val = booking[2]
            DF.increase(val , i , j)
        return DF.rst()
        