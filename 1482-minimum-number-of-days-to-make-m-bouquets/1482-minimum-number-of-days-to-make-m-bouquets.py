class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return - 1
        def canmakeK(days):
            count = 0
            bouquet = 0
            for day in bloomDay:
                if day <= days:
                    count += 1
                    if count == k:
                        bouquet += 1
                        count = 0
                else:
                    count = 0
            return bouquet >= m
        left , right = min(bloomDay) , max(bloomDay)
        while left < right:
            mid = (left + right) // 2
            if canmakeK(mid):
                right = mid 
            else:
                left = mid + 1
        return left
