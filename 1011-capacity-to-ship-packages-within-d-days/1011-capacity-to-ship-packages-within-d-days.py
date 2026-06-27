class Solution:
    def canfinish(self, weights , days , capacity):
        ship = 0
        c = 1
        for weight in weights:
            if ship + weight <= capacity:
                ship += weight
            else:
                c += 1
                ship = weight
        return c <= days


    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l , r = max(weights) , sum(weights)
        while l <= r:
            mid = (l + r) // 2
            if self.canfinish(weights , days , mid):
                r = mid - 1
            else:
                l = mid + 1
        return l
        
        