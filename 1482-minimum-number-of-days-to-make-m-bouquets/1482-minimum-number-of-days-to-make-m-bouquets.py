from bisect import bisect_left
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1
        n = len(bloomDay)
        ans = 0
        def isValid(mid):
            count = 0
            bouquet = 0
            for bloom in bloomDay:
                if bloom <= mid:
                    count += 1
                    if count == k:
                        count = 0
                        bouquet += 1
                        if bouquet >= m:
                            return True
                else:
                    count = 0
            return False

        left , right = min(bloomDay) , max(bloomDay)

        while left <= right:
            mid = (left + right) // 2
            if isValid(mid):
                right = mid - 1
            else:
                left = mid + 1
        
        return left



        