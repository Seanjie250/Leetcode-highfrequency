from bisect import bisect_left
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left , right = max(weights) , sum(weights)

        def is_ok(weights , capacity):
            used_day = 1
            w = 0
            for cur in weights:
                if cur + w <= capacity:
                    w += cur
                else:
                    used_day += 1
                    w = cur
                    if used_day > days:
                        return False
            print(used_day)
            print(capacity)
            return True
        
        while left <= right:
            mid = (left + right) // 2
            if is_ok(weights , mid):
                right = mid - 1
            else:
                left = mid + 1
        
        return left