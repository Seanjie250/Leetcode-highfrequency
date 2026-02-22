class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        ans = 0
        def is_ok(mid):
            count = 0
            bouquest = 0
            for day in bloomDay:
                if day <= mid:
                    count += 1
                    if count == k:
                        bouquest += 1
                        count = 0
                        if bouquest >= m:
                            return True
                else:
                    count = 0
            return False
        
        if m * k > len(bloomDay):
            return -1
        
        left , right = min(bloomDay) , max(bloomDay)
        while left <= right:
            mid = (left + right) // 2
            if is_ok(mid):
                ans = mid
                print(ans)
                right = mid - 1
            else:
                left = mid + 1
        return ans 
                    
            


        
        