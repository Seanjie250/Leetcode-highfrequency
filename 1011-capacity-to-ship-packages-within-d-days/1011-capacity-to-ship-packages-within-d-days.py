class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def countdays(capacity):
            count = 0
            total = 0
            for weight in weights:
                if total + weight > capacity:
                    count += 1
                    total = weight
                else:
                    total += weight
            if total > 0:
                count += 1
            return count
        left = min(weights)
        right = sum(weights)
        while left <= right:
            mid = (left + right) // 2
            time = countdays(mid)
            if time == days:
                return mid
            elif time > days:
                left = mid + 1
            else:
                right = mid - 1
        return left


        