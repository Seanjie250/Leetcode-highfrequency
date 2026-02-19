class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canFinish(k , piles , h):
            time = 0
            for pile in piles:
                time += pile // k
                if pile % k != 0:
                    time += 1
            if time <= h:
                return True
            else:
                return False
            
        left = 1 
        right = max(piles)
        max_ = float('-inf')
        while left <= right:
            mid = (left + right) // 2
            if canFinish(mid , piles ,h):
                max_ = mid
                right = mid - 1
            else:
                left = mid + 1
        return max_
            


        