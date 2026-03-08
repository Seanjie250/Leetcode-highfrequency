class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canfinish(piles , h , k):
            time = 0
            for pile in piles:
                time += pile // k
                pile = pile % k
                if pile > 0:
                    time += 1
                if time > h:
                    return False
            return True
        
        left = 1 
        right = max(piles)
        while left <= right:
            mid = (left + right) // 2
            if canfinish(piles , h , mid):
                right = mid - 1
            else:
                left  = mid + 1
        return left
        