class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canfinish(capacity):
            time = 0
            for pile in piles:
                time += pile // capacity
                pile = pile % capacity
                if pile > 0:
                    time += 1
            print(time)
            return time <= h
        left , right = 1 , max(piles)
        while left < right:
            mid = (left + right) // 2
            if canfinish(mid):
                right = mid
            else:
                left = mid + 1
        return left

