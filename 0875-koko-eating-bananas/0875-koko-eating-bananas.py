class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def is_ok(mid):
            time = 0
            for pile in piles:
                time += pile // mid
                if pile % mid > 0:
                    time += 1
                if time > h:
                    return False
            return True
        
        left , right = 1 , max(piles)
        while left <= right:
            mid = (left + right) // 2
            if is_ok(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left 