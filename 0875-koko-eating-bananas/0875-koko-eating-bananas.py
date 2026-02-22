class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canfinish(k):
            time = 0
            for pile in piles:
                time += pile // k
                if pile % k != 0:
                    time += 1
            if time > h:
                return False
            else:
                return True
        
        left = 1
        right = max(piles)
        max_ = float('-inf')
        while left <= right:
            mid = (right  + left ) // 2
            if canfinish(mid):
                max_= mid
                right  = mid - 1
            else:
                left = mid + 1
        return max_
        