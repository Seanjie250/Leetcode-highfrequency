class Solution:
    def canfinished(self , piles , k , h):
        time = 0
        for pile in piles:
            time += (pile + k - 1) // k
        return time <= h


    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l , r = 1 , max(piles)
        while l <= r:
            mid = (l + r) // 2
            if self.canfinished(piles , mid , h):
                r = mid - 1
            else:
                l = mid + 1
        return l



        