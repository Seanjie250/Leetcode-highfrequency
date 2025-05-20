# Last updated: 5/20/2025, 3:57:30 PM
from collections import deque
def update_the_q(kept_self,nums):
        while kept_self and kept_self[-1] < nums:
            kept_self.pop()
        kept_self.append(nums)
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maximum = deque()
        record = []
        for i in range(len(nums)):
            update_the_q(maximum,nums[i])
            if i >= k  and nums[i - k] == maximum[0]:
                maximum.popleft()
            if i >= k -1 :
                record.append(maximum[0])
        return record

        


            
        


        


            
            



        